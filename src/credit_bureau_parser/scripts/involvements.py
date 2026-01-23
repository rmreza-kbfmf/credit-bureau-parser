from credit_bureau_parser.utils.parser_utils import (
    get_nested_dict,
    get_sql_text,
    get_field_value,
    get_amount,
    set_field_value,
    is_object,
    get_sql_field_values_list
)

from credit_bureau_parser.utils.decorator_utils import safe_run
# from utils.logger_utils import get_logger

from credit_bureau_parser.scripts.base_processor import BaseProcessor  

import pandas as pd
from tqdm import tqdm

class InvolvementProcessor(BaseProcessor):
    @safe_run(use_logger=False)    
    def process(self, output_format=None):
        # Define sections and corresponding feature lists
        self.sections = [
            (self.feature_set.INVOLVEMENTS_SUMMARY_ROOT, self.feature_set.INVOLVEMENTS_SUMMARY),
        ]    

        self.subsections = []    

        sql_field, sql_values = set_field_value(self.filename)
        for section_key, fields in self.sections:
            data = get_nested_dict(self.root, section_key)
            if data is None: # If no data found, we fill the field with None. 
                sql_field, sql_values = self._extract_fields(data, fields, sql_field, sql_values, none_data=True)
                continue    

            for tempdata in data:    
                sql_field, sql_values = self._extract_fields(tempdata, fields, sql_field, sql_values)

        # Recurse into sub-sections
        self._process_result(
            parent=self.root,
            inherited_fields=(sql_field, sql_values)
        )

        self.save_output(output_format=output_format)
        return self.sql_field_list, self.sql_values_list               