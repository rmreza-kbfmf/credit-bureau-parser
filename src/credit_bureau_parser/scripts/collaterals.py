from credit_bureau_parser.utils.parser_utils import (
    get_sql_text,
    get_field_value,
    get_amount,
    set_field_value,
    is_object,
    get_sql_field_values_list,
    get_nested_dict,
    normalize_to_list
)

from credit_bureau_parser.utils.decorator_utils import safe_run
# from utils.logger_utils import get_logger

from credit_bureau_parser.scripts.base_processor import BaseProcessor  

import pandas as pd
from tqdm import tqdm

class ContractCollateralProcessor(BaseProcessor):
    @safe_run(use_logger=False)
    def process(self, output_format=None):
        self.sections = [
            (self.feature_set.INDIVIDUAL_IDENTIFICATION_ROOT, self.feature_set.INDIVIDUAL_PEFINDO_ID),
            (self.feature_set.CONTRACTS_ROOT, self.feature_set.CONTRACT_CORE_KEY)
        ]

        self.subsections = [
            (self.feature_set.COLLATERAL_ROOT, self.feature_set.CONTRACT_COLLATERAL)
        ]

        base_sql_field = None
        base_sql_values = None

        for section_key, fields in self.sections:
            data = get_nested_dict(self.root, section_key)

            # 🔑 normalize parent rows
            parent_list = data if data not in (None, [], {}) else [None]

            # --- identification section (singleton, no row emission)
            if section_key == self.feature_set.INDIVIDUAL_IDENTIFICATION_ROOT:
                parent = parent_list[0]  # only one logical parent
                base_sql_field, base_sql_values = set_field_value(self.filename)
                base_sql_field, base_sql_values = self._extract_fields(
                    parent,
                    fields,
                    base_sql_field,
                    base_sql_values,
                    none_data=(parent is None),
                )
                continue

            # --- contract section (row-driving)
            for parent in parent_list:
                # start from base (filename + pefindo id)
                sql_field, sql_values = base_sql_field, base_sql_values

                sql_field, sql_values = self._extract_fields(
                    parent,
                    fields,
                    sql_field,
                    sql_values,
                    none_data=(parent is None),
                )

                # 🔥 subsection (collateral) fully handled by BaseProcessor
                self._process_result(
                    parent=parent if parent is not None else self.root,
                    inherited_fields=(sql_field, sql_values),
                )

        self.save_output(output_format=output_format)
        return self.sql_field_list, self.sql_values_list