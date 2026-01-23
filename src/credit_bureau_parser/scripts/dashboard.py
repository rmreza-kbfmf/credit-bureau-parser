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

class DashboardProcessor(BaseProcessor):
    @safe_run(use_logger=False)    
    def process(self, output_format=None):
        # Define sections and corresponding feature lists
        self.sections = [
            (self.feature_set.DASHBOARD_CIQ_ROOT, self.feature_set.DASHBOARD_CIQ),
            (self.feature_set.DASHBOARD_COLLATERALS_ROOT, self.feature_set.DASHBOARD_COLLATERALS),
            (self.feature_set.DASHBOARD_DISPUTES_ROOT, self.feature_set.DASHBOARD_DISPUTES),
            (self.feature_set.DASHBOARD_INQUIRIES_ROOT, self.feature_set.DASHBOARD_INQUIRIES),
            (self.feature_set.DASHBOARD_INVOLVEMENTS_ROOT, self.feature_set.DASHBOARD_INVOLVEMENTS),
            (self.feature_set.DASHBOARD_OTHER_LIABILITIES_ROOT, self.feature_set.DASHBOARD_OTHER_LIABILITIES),
            (self.feature_set.DASHBOARD_PAYMENTS_PROFILE_ROOT, self.feature_set.DASHBOARD_PAYMENTS_PROFILE),
            (self.feature_set.DASHBOARD_RELATIONS_ROOT, self.feature_set.DASHBOARD_RELATIONS),
            (self.feature_set.DASHBOARD_SECURITIES_ROOT, self.feature_set.DASHBOARD_SECURITIES),
        ]
        self.subsections = []    

        sql_field, sql_values = set_field_value(self.filename)
        for section_key, fields in self.sections:
            data = get_nested_dict(self.root, section_key)
            if data is None:
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