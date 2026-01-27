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
    def __init__(self, root, filename, folder_path, foldername='output',
                 processor_name=None, data_type='xml', use_multiprocessing=False):
        self.root = root
        self.filename = filename
        self.folder_path = folder_path
        self.foldername = f"{foldername}/{data_type.lower()}"
        self.sql_field_list = []
        self.sql_values_list = []
        self.sections = []
        self.subsections = []
        self.data_type = data_type.lower()
        self.use_multiprocessing = use_multiprocessing

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
        except Exception:
            self.table_name = 'Default'

    # ------------------------------------------------------------------
    # 🔑 ADDITIVE helper (no variable changes)
    # ------------------------------------------------------------------
    def _with_optional_lock(self, lock_path, fn):
        """
        Use FileLock ONLY when multiprocessing is enabled.
        """
        if self.use_multiprocessing:
            lock = FileLock(lock_path)
            with lock:
                fn()
        else:
            fn()

    # ------------------------------------------------------------------
    # EVERYTHING BELOW IS UNCHANGED
    # ------------------------------------------------------------------
    def _extractor(self, field, record, sql_field, sql_values, none_data=False):
        if none_data:
            if field in self.feature_set.FIELD_ADDRESS:
                for sub_field in self.feature_set.INDIVIDUAL_ADDRESS:
                    combined_field = f"{field}_{sub_field}"
                    sql_field, sql_values = get_field_value(
                        None, combined_field, sql_field, sql_values, field_int=[]
                    )

            elif field in self.feature_set.FIELD_CONTACT:
                for sub_field in self.feature_set.INDIVIDUAL_CONTACT:
                    combined_field = f"{field}_{sub_field}"
                    sql_field, sql_values = get_field_value(
                        None, combined_field, sql_field, sql_values, field_int=[]
                    )

            else:
                sql_field, sql_values = get_field_value(
                    None, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT
                )
            return sql_field, sql_values
        else:
            if field in self.feature_set.FIELD_ADDRESS:
                address_list = record.get(field, []) or []
                address = address_list[0] if isinstance(address_list, list) and address_list else {}
                for sub_field in self.feature_set.INDIVIDUAL_ADDRESS:
                    combined_field = f"{field}_{sub_field}"
                    nested_value = address.get(sub_field) if isinstance(address, dict) else None
                    sql_field, sql_values = get_field_value(
                        nested_value, combined_field, sql_field, sql_values, field_int=[]
                    )

            elif field in self.feature_set.FIELD_CONTACT:
                contact_list = record.get(field, []) or []
                contact = contact_list[0] if isinstance(contact_list, list) and contact_list else {}
                for sub_field in self.feature_set.INDIVIDUAL_CONTACT:
                    combined_field = f"{field}_{sub_field}"
                    nested_value = contact.get(sub_field) if isinstance(contact, dict) else None
                    sql_field, sql_values = get_field_value(
                        nested_value, combined_field, sql_field, sql_values, field_int=[]
                    )

            elif field in self.feature_set.FIELD_AMOUNT:
                nested_value = get_nested_dict(record, [field, self.feature_set.LOCAL_VALUE])
                sql_field, sql_values = get_field_value(
                    nested_value, field, sql_field, sql_values, field_int=self.feature_set.FIELD_AMOUNT
                )

            elif field in self.feature_set.FIELD_DATE:
                value = is_object(field, record)
                value = value[0:10]
                sql_field, sql_values = get_field_value(value, field, sql_field, sql_values, field_int=[])




            else:
                value = is_object(field, record)
                sql_field, sql_values = get_field_value(
                    value, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT
                )

            return sql_field, sql_values

    def _rename_field(self, field, old_value, new_value):
        return field.replace(old_value, new_value)


    def _extract_fields(self, record, fields, sql_field, sql_values, none_data=False):
        if none_data:
            for field in fields:
                sql_field, sql_values = self._extractor(
                    field, record, sql_field, sql_values, none_data=True
                )
        else:
            for field in fields:
                try:
                    sql_field, sql_values = self._extractor(
                        field, record, sql_field, sql_values, none_data=False
                    )
                except Exception:
                    sql_field, sql_values = get_field_value(
                        None, field, sql_field, sql_values, field_int=self.feature_set.FIELD_INT
                    )

        sql_field = self._rename_field(sql_field, "IdScoreId", "PefindoId")
        return sql_field, sql_values

    def _process_result(self, parent, inherited_fields):
        self.subsections = [(x, y) for x, y in self.subsections if x or y]
        if not self.subsections:
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

    def save_output(self, auto_increment=False, output_format=None,
                    compression='snappy', parquet_engine="pyarrow"):

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
            if not self.sql_field_list:
                return

            raw_header = self.sql_field_list[-1]
            header = "ID," + ",".join(raw_header) if auto_increment else ",".join(raw_header)
            header_csv = header

            rows = []
            for i, row in enumerate(self.sql_values_list, start=1):
                row_values = [normalize_value(v) for v in row]
                if auto_increment:
                    row_values = [i] + list(row)
                rows.append(row_values)

            output_folder = self.folder_path
            os.makedirs(output_folder, exist_ok=True)

            output_filename = f"{output_folder}/{self.table_name}.csv"
            lock_path = f"{output_filename}.lock"
            created_at = pd.Timestamp.now()

            def write_csv():
                file_exists = os.path.exists(output_filename)
                header_with_created = header_csv + ",CreatedAt" if header_csv else ""

                with open(output_filename, "a", encoding="utf-8") as f:
                    if not file_exists:
                        f.write(header_with_created + "\n")
                    for row in rows:
                        formatted = format_row_with_timestamp(row, created_at)
                        if formatted:
                            f.write(formatted + "\n")

            self._with_optional_lock(lock_path, write_csv)

            if output_format == "parquet":
                output_parquet_path = f"{output_folder}/{self.table_name}.parquet"
                parquet_lock = f"{output_parquet_path}.lock"

                def write_parquet():
                    df = pd.read_csv(output_filename, low_memory=False)
                    df.to_parquet(
                        output_parquet_path,
                        index=False,
                        compression=compression,
                        engine=parquet_engine,
                    )
                    del df
                    gc.collect()

                self._with_optional_lock(parquet_lock, write_parquet)
        except Exception as e:
            print(f"[{self.processor_name}] ❌ ERROR saving output: {e}")