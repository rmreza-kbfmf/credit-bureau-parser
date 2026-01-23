import gc

from pathlib import Path
from filelock import FileLock
from credit_bureau_parser.utils.parser_utils import format_value
from credit_bureau_parser.config.constant import PefindoFeatures
from credit_bureau_parser.config.constant_json import PefindoFeatures as PefindoFeaturesJSON

from credit_bureau_parser.utils.parser_utils import (
    get_nested_dict,
    get_sql_text,
    get_field_value,
    get_amount,
    set_field_value,
    is_object,
    get_sql_field_values_list,
    format_row_with_timestamp,
    normalize_to_list)

import os
import pandas as pd
import csv

class BaseProcessor:
    def __init__(self, root, filename, folder_path, foldername = 'output', processor_name=None, 
                 data_type='xml'):
        self.root = root
        self.filename = filename
        self.folder_path = folder_path
        self.foldername = f"{foldername}/{data_type.lower()}"
        self.sql_field_list = []
        self.sql_values_list = []
        self.sections = []
        self.subsections = []
        self.data_type = data_type.lower()

        # Choose feature set once here
        if self.data_type == "xml":
            self.feature_set = PefindoFeatures
        else:
            self.feature_set = PefindoFeaturesJSON

        if not processor_name:
            self.processor_name = self.__class__.__name__  
        else:
            self.processor_name = processor_name  

        try:
            self.table_name = self.processor_name.split("Processor")[0]
        except Exception as e:
            self.table_name = 'Default'

    def _extractor(self, field, record, sql_field, sql_values, none_data=False):
        if none_data:
            if field in self.feature_set.FIELD_ADDRESS:
                for sub_field in self.feature_set.INDIVIDUAL_ADDRESS:
                        combined_field = f"{field}_{sub_field}"
                        sql_field, sql_values = get_field_value(None, combined_field, sql_field, sql_values, field_int=[])

            elif field in self.feature_set.FIELD_CONTACT:
                for sub_field in self.feature_set.INDIVIDUAL_CONTACT:
                        combined_field = f"{field}_{sub_field}"
                        sql_field, sql_values = get_field_value(None, combined_field, sql_field, sql_values, field_int=[])

            else:
                sql_field, sql_values = get_field_value(None, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT)
            
            return sql_field, sql_values
        else:
            if field in self.feature_set.FIELD_ADDRESS:
                address_list = record.get(field, []) or []
                address = address_list[0] if isinstance(address_list, list) and address_list else {}
                for sub_field in self.feature_set.INDIVIDUAL_ADDRESS:
                    combined_field = f"{field}_{sub_field}"
                    nested_value = address.get(sub_field) if isinstance(address, dict) else None
                    sql_field, sql_values = get_field_value(nested_value, combined_field, sql_field, sql_values, field_int=[])

            elif field in self.feature_set.FIELD_CONTACT:
                contact_list = record.get(field, []) or []
                contact = contact_list[0] if isinstance(contact_list, list) and contact_list else {}
                for sub_field in self.feature_set.INDIVIDUAL_CONTACT:
                    combined_field = f"{field}_{sub_field}"
                    nested_value = contact.get(sub_field) if isinstance(contact, dict) else None
                    sql_field, sql_values = get_field_value(nested_value, combined_field, sql_field, sql_values, field_int=[])

            elif field in self.feature_set.FIELD_AMOUNT:
                nested_value = get_nested_dict(record, [field, self.feature_set.LOCAL_VALUE])
                sql_field, sql_values = get_field_value(nested_value, field, sql_field, sql_values, field_int=self.feature_set.FIELD_AMOUNT)

            elif field in self.feature_set.FIELD_DATE:
                value = is_object(field, record)
                value = value[0:10]
                sql_field, sql_values = get_field_value(value, field, sql_field, sql_values, field_int=[])




            else:
                value = is_object(field, record)
                sql_field, sql_values = get_field_value(value, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT)

            return sql_field, sql_values

    def _rename_field(self, field, old_value, new_value):
        return field.replace(old_value, new_value)


    def _extract_fields(self, record, fields, sql_field, sql_values, none_data=False):
        if none_data:
            for field in fields:
                sql_field, sql_values = self._extractor(field, record, sql_field, sql_values, none_data=True)
            
        else:
            for field in fields:
                try:
                    sql_field, sql_values = self._extractor(field, record, sql_field, sql_values, none_data=False)

                except Exception as e:
                    print(f"[{self.__class__.__name__}] extract_fields error: {e}")
                    sql_field, sql_values = get_field_value(None, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT)

        sql_field = self._rename_field(sql_field, "IdScoreId", "PefindoId")
        return sql_field, sql_values  
     
    def _process_result(self, parent, inherited_fields):
        """Recursively process nested sections"""
        # to handle all none data make into empty list
        self.subsections = [(x, y) for x, y in self.subsections if x or y]
        if not self.subsections:
            # No subsections: directly extract and save
            sql_field, sql_values = inherited_fields
            get_sql_text(self.table_name, sql_field, sql_values)
            self.sql_field_list, self.sql_values_list = get_sql_field_values_list(
                sql_field, sql_values, self.sql_field_list, self.sql_values_list
            )
            return

        for sub_section_key, sub_fields in self.subsections:
            sub_data = get_nested_dict(parent, sub_section_key)
            if sub_data is None:
                continue

            for sub_tempdata in sub_data:
                sub_sql_field, sub_sql_values = inherited_fields
                sub_sql_field, sub_sql_values = self._extract_fields(
                    sub_tempdata, sub_fields, sub_sql_field, sub_sql_values
                )

                get_sql_text(self.table_name, sub_sql_field, sub_sql_values)
                self.sql_field_list, self.sql_values_list = get_sql_field_values_list(
                    sub_sql_field, sub_sql_values, self.sql_field_list, self.sql_values_list
                )

    def save_output(self, auto_increment=False, output_format=None, compression='snappy', parquet_engine="pyarrow"):
        def normalize_value(v):
            if v is None or v == "NULL":
                return None
            if isinstance(v, str):
                try:
                    if "." in v:
                        f = float(v)
                        if f.is_integer():
                            return int(f)
                        return f
                    return int(v)
                except ValueError:
                    return v
            return v

        try:
            # ===== Skip if no header fields =====
            if not self.sql_field_list:
                return

            # ===== Shared header and rows preparation =====
            raw_header = self.sql_field_list[-1]
            if auto_increment:
                header = "ID," + ",".join(raw_header)
            else:
                header = ",".join(raw_header)
            header_csv = header

            rows = []
            for i, row in enumerate(self.sql_values_list, start=1):
                try:
                    row_values = [normalize_value(v) for v in row]
                    if auto_increment:
                        row_values = [i] + list(row_values)
                    rows.append(row_values)
                except Exception as e:
                    print(f"❌ Error preparing row {i}: {row}")
                    print(f"⚠️ Exception: {e}")

            # ===== CSV Output =====
            # Build full folder path
            output_folder = self.folder_path
            
            # ✅ Ensure folder exists
            os.makedirs(output_folder, exist_ok=True)            

            output_filename = f"{output_folder}/{self.table_name}.csv"
            lock = FileLock(f"{output_filename}.lock")

            created_at = pd.Timestamp.now()
            #handle header_csv
            if header_csv:
                header_with_created = header_csv + ",CreatedAt"
            else:
                header_with_created = ""


            row_strings = [
                formatted for row in rows
                if (formatted := format_row_with_timestamp(row, created_at)) is not None
            ]


            with lock:
                file_exists = os.path.exists(output_filename)
                header_already_written = False
                if file_exists:
                    with open(output_filename, "r", encoding="utf-8") as f:
                        first_line = f.readline().strip()
                        #handle first line of header with : 
                        #1. check header already created
                        #2. check header empty due to file doesnt have those tags
                        header_already_written = (first_line == header_with_created or not header_with_created)

                with open(output_filename, "a", encoding="utf-8") as f:
                    if not file_exists or not header_already_written:
                        f.write(header_with_created + "\n")
                    for row_str in row_strings:
                        try:
                            f.write(row_str + "\n")
                        except Exception as e:
                            print(f"❌ Error writing row: {row_str}")
                            print(f"⚠️ Exception: {e}")

            # ===== Parquet Output (Partitioned) =====
            print(output_format)
            if output_format == "parquet":
                output_csv_path = os.path.join(output_folder, f"{self.table_name}.csv")
                output_parquet_path = os.path.join(output_folder, f"{self.table_name}.parquet")

                if not os.path.exists(output_csv_path):
                    raise FileNotFoundError(f"CSV file not found: {output_csv_path}")

                try:
                    df = pd.read_csv(output_csv_path, low_memory=False)

                    lock = FileLock(f"{output_parquet_path}.lock")
                    with lock:
                        df.to_parquet(output_parquet_path, index=False, compression=compression, engine=parquet_engine)

                    # Clean up memory
                    del df
                    gc.collect()

                except Exception as e:
                    print(f"[{self.processor_name}] ❌ ERROR during parquet conversion: {e}")

        except Exception as e:
            print(f"[{self.processor_name}] ❌ ERROR saving output: {e}")