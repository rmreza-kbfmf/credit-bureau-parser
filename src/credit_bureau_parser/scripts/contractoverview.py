from credit_bureau_parser.utils.parser_utils import (
    get_nested_dict,
    get_sql_text,
    get_field_value,
    get_amount,
    set_field_value,
    is_object,
    get_sql_field_values_list,
    normalize_to_list
)

from credit_bureau_parser.utils.decorator_utils import safe_run
# from utils.logger_utils import get_logger

from credit_bureau_parser.scripts.base_processor import BaseProcessor  

import pandas as pd
from tqdm import tqdm

class ContractOverviewProcessor(BaseProcessor):
    @safe_run(use_logger=False)
    def process(self, output_format=None):
        self.sections = [
            (self.feature_set.CONTRACT_OVERVIEW_ROOT, self.feature_set.CONTRACT_OVERVIEW)
        ]

        self.subsections = []

        sql_field, sql_values = set_field_value(self.filename) 

        for section_key, fields in self.sections:
            data = get_nested_dict(self.root, section_key)      
            if data is None:
                sql_field, sql_values = self._extract_fields(data, fields, sql_field, sql_values, none_data=True)
                self._process_result(
                parent=self.root,
                inherited_fields=(sql_field, sql_values)
                )     
                continue

            for tempdata in data:                
                sql_field, sql_values = set_field_value(self.filename)
                sql_field, sql_values = self._extract_fields(tempdata, fields, sql_field, sql_values)

                # Recurse into sub-sections
                self._process_result(
                    parent=tempdata,
                    inherited_fields=(sql_field, sql_values)
                )

        self.save_output(auto_increment=False, output_format=output_format)
        return self.sql_field_list, self.sql_values_list