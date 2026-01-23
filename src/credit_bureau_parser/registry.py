from credit_bureau_parser.config.constant import PefindoFeatures
from credit_bureau_parser.config.constant_json import (
    PefindoFeatures as PefindoFeaturesJSON
)

FEATURE_REGISTRY = {
    "pefindo" : {
        "xml": PefindoFeatures,
        "json": PefindoFeaturesJSON
    }
}


def get_feature_set(bureau_name: str, data_type: str):
    """
    Resolve feature set based on data_type
    """
    try:
        return FEATURE_REGISTRY[bureau_name][data_type]
    except KeyError:
        raise ValueError(
            f"Unsupported data_type '{data_type}'. "
            f"Available: {list(FEATURE_REGISTRY.keys())}"
        )


# =========================
# Processor Registry
# =========================

from credit_bureau_parser.scripts.cip import CIPProcessor
from credit_bureau_parser.scripts.contractoverview import ContractOverviewProcessor
from credit_bureau_parser.scripts.collaterals import ContractCollateralProcessor
from credit_bureau_parser.scripts.contractpaymentcalendar import (
    ContractPaymentCalendarProcessor,
)
from credit_bureau_parser.scripts.contractsummary import (
    ContractSummaryDebtorProcessor,
    ContractSummaryOverallProcessor,
    ContractSummaryPaymentCalendarProcessor,
)
from credit_bureau_parser.scripts.contracts import ContractProcessor
from credit_bureau_parser.scripts.inquiries import (
    InquiriesProcessor,
    InquiriesSummaryProcessor,
)
from credit_bureau_parser.scripts.individuals import IndividualProcessor
from credit_bureau_parser.scripts.parameters import ParametersProcessor
from credit_bureau_parser.scripts.subjectinfohistory import SubjectInfoListProcessor
from credit_bureau_parser.scripts.currentrelations import (
    CurrentRelationsRelatedPartyProcessor,
)


PROCESSOR_REGISTRY = {
    "default": [
        InquiriesProcessor,
        InquiriesSummaryProcessor,
        CIPProcessor,
        ContractOverviewProcessor,
        ContractCollateralProcessor,
        ContractPaymentCalendarProcessor,
        ContractSummaryDebtorProcessor,
        ContractSummaryOverallProcessor,
        ContractSummaryPaymentCalendarProcessor,
        ContractProcessor,
        IndividualProcessor,
        ParametersProcessor,
        SubjectInfoListProcessor,
        CurrentRelationsRelatedPartyProcessor,
    ],

    # example extension
    "light": [
        InquiriesProcessor,
        CIPProcessor,
        ContractProcessor,
    ],
}


def get_processors(processor_set: str = "default"):
    """
    Resolve processors based on processor_set name
    """
    try:
        return PROCESSOR_REGISTRY[processor_set]
    except KeyError:
        raise ValueError(
            f"Unknown processor_set '{processor_set}'. "
            f"Available: {list(PROCESSOR_REGISTRY.keys())}"
        )