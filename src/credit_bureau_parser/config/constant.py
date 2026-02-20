class PefindoFeatures():
    #Version 5.69

# ---------------------------------------
#                ENVELOPE
# ---------------------------------------

    ENVELOPE_TAG = "Envelope"
    BODY_TAG = "Body"
    CUSTOM_REPORT_RESPONSE_TAG = "GetCustomReportResponse"
    CUSTOM_REPORT_RESULT_TAG = "GetCustomReportResult"

    ROOT = [ENVELOPE_TAG, BODY_TAG, CUSTOM_REPORT_RESPONSE_TAG, CUSTOM_REPORT_RESULT_TAG]

# Main root of the XML document

# ---------------------------------------
#                  CIP
# ---------------------------------------

    CIP_TAG = "CIP"
    CIP_RECORDLIST_TAG = "RecordList"
    CIP_RECORD_TAG = "Record"
    CIP_REASONSLIST_TAG = "ReasonsList"
    CIP_REASON_TAG = "Reason"

    CIP_ROOT = [CIP_TAG, CIP_RECORDLIST_TAG, CIP_RECORD_TAG]
    CIP_REASON_ROOT = [CIP_REASONSLIST_TAG, CIP_REASON_TAG]

# ---------------------------------------
#                  CIQ
# ---------------------------------------

    CIQ_TAG = "CIQ"
    CIQ_DETAIL_TAG = "Detail"
    CIP_SUMMARY_TAG = "Summary"
    CIQ_DETAIL_ROOT = [CIQ_TAG, CIQ_DETAIL_TAG]
    CIQ_SUMMARY_ROOT = [CIQ_TAG, CIP_SUMMARY_TAG]

# ---------------------------------------
#              CONTRACTS
# ---------------------------------------

    CONTRACTS_TAG = "Contracts"
    CONTRACTS_LIST_TAG = "ContractList"
    CONTRACT_TAG = "Contract"
    CONTRACT_CODE_TAG = "ContractCode"
    CONTRACT_CREDITOR_TAG = "Creditor"
    CONTRACTS_ROOT = [CONTRACTS_TAG, CONTRACTS_LIST_TAG, CONTRACT_TAG]

# ---------------------------------------
#            CONTRACT SUMMARY
# ---------------------------------------

    CONTRACT_SUMMARY_TAG = "ContractSummary"
    CONTRACT_SUMMARY_DEBTOR_TAG = "Debtor"
    CONTRACT_SUMMARY_GUARANTOR_TAG = "Guarantor"
    CONTRACT_SUMMARY_OVERALL_TAG = "Overall"
    CONTRACT_SUMMARY_PAYMENT_CALENDAR_LIST_TAG = "PaymentCalendarList"
    CONTRACT_SUMMARY_PAYMENT_CALENDAR_TAG = "PaymentCalendar"
    CONTRACT_SUMMARY_SECTOR_INFO_LIST_TAG = "SectorInfoList"
    CONTRACT_SUMMARY_SECTOR_INFO_TAG = "SectorInfo"

    CONTRACT_SUMMARY_ROOT = [CONTRACT_SUMMARY_TAG]
    CONTRACT_SUMMARY_DEBTOR_ROOT = [CONTRACT_SUMMARY_TAG, CONTRACT_SUMMARY_DEBTOR_TAG]
    CONTRACT_SUMMARY_GUARANTOR_ROOT = [CONTRACT_SUMMARY_TAG, CONTRACT_SUMMARY_GUARANTOR_TAG]
    CONTRACT_SUMMARY_OVERALL_ROOT = [CONTRACT_SUMMARY_TAG, CONTRACT_SUMMARY_OVERALL_TAG]
    CONTRACT_SUMMARY_PAYMENT_CALENDAR_ROOT = [CONTRACT_SUMMARY_TAG, CONTRACT_SUMMARY_PAYMENT_CALENDAR_LIST_TAG, CONTRACT_SUMMARY_PAYMENT_CALENDAR_TAG]
    CONTRACT_SUMMARY_SECTOR_INFO_ROOT = [CONTRACT_SUMMARY_TAG, CONTRACT_SUMMARY_SECTOR_INFO_LIST_TAG, CONTRACT_SUMMARY_SECTOR_INFO_TAG]

# ---------------------------------------
#            CONTRACT OVERVIEW
# ---------------------------------------

    CONTRACT_OVERVIEW_TAG = "ContractOverview"
    CONTRACT_OVERVIEW_LIST_TAG = "ContractList"
    CONTRACT_OVERVIEW_CONTRACT_TAG = "Contract"

    CONTRACT_OVERVIEW_ROOT = [CONTRACT_OVERVIEW_TAG, CONTRACT_OVERVIEW_LIST_TAG, CONTRACT_OVERVIEW_CONTRACT_TAG]

# ---------------------------------------
#              COLLARETAL
# ---------------------------------------

    COLLATERALS_LIST_TAG = "CollateralsList"
    COLLATERAL_TAG = "Collateral"

    COLLATERAL_ROOT = [COLLATERALS_LIST_TAG, COLLATERAL_TAG]

# ---------------------------------------
#         PAYMENT CALENDAR
# ---------------------------------------

    PAYMENT_CALENDAR_LIST_TAG = "PaymentCalendarList"
    CALENDAR_TAG = "CalendarItem"

    PAYMENT_CALENDAR_ROOT = [PAYMENT_CALENDAR_LIST_TAG, CALENDAR_TAG]

# ---------------------------------------
#              INDIVIDUAL
# ---------------------------------------

    INDIVIDUAL_TAG = "Individual"
    INDIVIDUAL_CONTACT_TAG = "Contact"
    INDIVIDUAL_GENERAL_TAG = "General"
    INDIVIDUAL_IDENTIFICATION_TAG = "Identifications"
    INDIVIDUAL_ADDRESS_TAG = "MainAddress"

    INDIVIDUAL_ROOT = [INDIVIDUAL_TAG]
    INDIVIDUAL_CONTACT_ROOT = [INDIVIDUAL_TAG, INDIVIDUAL_CONTACT_TAG]
    INDIVIDUAL_GENERAL_ROOT = [INDIVIDUAL_TAG, INDIVIDUAL_GENERAL_TAG]
    INDIVIDUAL_IDENTIFICATION_ROOT = [INDIVIDUAL_TAG, INDIVIDUAL_IDENTIFICATION_TAG]
    INDIVIDUAL_ADDRESS_ROOT = [INDIVIDUAL_TAG, INDIVIDUAL_ADDRESS_TAG]

# ---------------------------------------
#              INQUIRIES
# ---------------------------------------

    INQUIRIES_TAG = "Inquiries"
    INQUIRIES_SUMMARY_TAG = "Summary"
    INQUIRIES_INQUIRYLIST_TAG = "InquiryList"
    INQUIRIES_INQUIRY_TAG = "Inquiry"


    INQUIRIES_SUMMARY_ROOT = [INQUIRIES_TAG, INQUIRIES_SUMMARY_TAG]
    INQUIRIES_INQUIRYLIST_ROOT = [INQUIRIES_TAG, INQUIRIES_INQUIRYLIST_TAG, INQUIRIES_INQUIRY_TAG]

# ---------------------------------------
#              REPORT INFO
# ---------------------------------------

    REPORT_INFO_TAG = "ReportInfo"

    REPORT_INFO_ROOT = [REPORT_INFO_TAG]

# ---------------------------------------
#              INVOLVEMENTS
# ---------------------------------------

    INVOLVEMENTS_TAG = "Involvements"
    INVOLVEMENTS_SUMMARY_TAG = "Summary"

    INVOLVEMENTS_SUMMARY_ROOT = [INVOLVEMENTS_TAG, INVOLVEMENTS_SUMMARY_TAG]

# ---------------------------------------
#               PARAMETERS
# ---------------------------------------

    PARAMETERS_TAG = "Parameters"
    
    PARAMETERS_ROOT = [PARAMETERS_TAG]

# ---------------------------------------
#               SECURITIES
# ---------------------------------------

    SECURITIES_TAG = "Securities"
    SECURITIES_SUMMARY_TAG = "Summary"
    
    SECURITIES_SUMMARY_ROOT = [SECURITIES_TAG, SECURITIES_SUMMARY_TAG]

# ---------------------------------------
#          SUBJECT INFO HISTORY
# ---------------------------------------

    SUBJECT_INFO_HISTORY_TAG = "SubjectInfoHistory"
    SUBJECT_INFO_ADDRESS_LIST_TAG = "AddressList"
    SUBJECT_INFO_ADDRESS_TAG = "Address"
    SUBJECT_INFO_CONTACT_LIST_TAG = "ContactList"
    SUBJECT_INFO_CONTACT_TAG = "Contact"
    SUBJECT_INFO_GENERAL_LIST_TAG = "GeneralList"
    SUBJECT_INFO_GENERAL_TAG = "General"
    SUBJECT_INFO_IDENTIFICATION_LIST_TAG = "IdentificationsList"
    SUBJECT_INFO_IDENTIFICATION_TAG = "Identifications"
    
    SUBJECT_INFO_LIST_ROOT = [SUBJECT_INFO_HISTORY_TAG]
    # SUBJECT_INFO_ADDRESS_LIST_ROOT = [SUBJECT_INFO_HISTORY_TAG, SUBJECT_INFO_ADDRESS_LIST_TAG, SUBJECT_INFO_ADDRESS_TAG]
    # SUBJECT_INFO_CONTACT_LIST_ROOT = [SUBJECT_INFO_HISTORY_TAG, SUBJECT_INFO_CONTACT_LIST_TAG, SUBJECT_INFO_CONTACT_TAG]
    # SUBJECT_INFO_GENERAL_LIST_ROOT = [SUBJECT_INFO_HISTORY_TAG, SUBJECT_INFO_GENERAL_LIST_TAG, SUBJECT_INFO_GENERAL_TAG]
    # SUBJECT_INFO_IDENTIFICATION_LIST_ROOT = [SUBJECT_INFO_HISTORY_TAG, SUBJECT_INFO_IDENTIFICATION_LIST_TAG, SUBJECT_INFO_IDENTIFICATION_TAG]

    SUBJECT_INFO_ADDRESS_LIST_ROOT = [SUBJECT_INFO_ADDRESS_LIST_TAG, SUBJECT_INFO_ADDRESS_TAG]
    SUBJECT_INFO_CONTACT_LIST_ROOT = [SUBJECT_INFO_CONTACT_LIST_TAG, SUBJECT_INFO_CONTACT_TAG]
    SUBJECT_INFO_GENERAL_LIST_ROOT = [SUBJECT_INFO_GENERAL_LIST_TAG, SUBJECT_INFO_GENERAL_TAG]
    SUBJECT_INFO_IDENTIFICATION_LIST_ROOT = [SUBJECT_INFO_IDENTIFICATION_LIST_TAG, SUBJECT_INFO_IDENTIFICATION_TAG]





# ---------------------------------------
#          CURRENT RELATIONS
# ---------------------------------------

    CURRENT_RELATIONS_TAG = "CurrentRelations"
    CURRENT_RELATIONS_CONTRACT_RELATION_LIST_TAG = "ContractRelationList"
    CURRENT_RELATIONS_RELATED_PARTY_LIST_TAG = "RelatedPartyList"
    CURRENT_RELATIONS_RELATED_PARTY_TAG = "RelatedParty"
    CURRENT_RELATIONS_CONTRACT_RELATION_TAG = "ContractRelation"
    CURRENT_RELATIONS_CONTACT_TAG = "Contact"
    CURRENT_RELATIONS_MAIN_ADDRESS_TAG = "Address"
    
    CURRENT_RELATIONS_CONTRACT_RELATION_ROOT = [CURRENT_RELATIONS_TAG, CURRENT_RELATIONS_CONTRACT_RELATION_LIST_TAG, CURRENT_RELATIONS_CONTRACT_RELATION_TAG]
    CURRENT_RELATIONS_CONTACT_TAG_ROOT = [CURRENT_RELATIONS_CONTRACT_RELATION_ROOT, CURRENT_RELATIONS_CONTACT_TAG]
    CURRENT_RELATIONS_MAIN_ADDRESS_TAG_ROOT = [CURRENT_RELATIONS_CONTRACT_RELATION_ROOT, CURRENT_RELATIONS_MAIN_ADDRESS_TAG]
    CURRENT_RELATIONS_RELATED_PARTY_ROOT = [CURRENT_RELATIONS_TAG, CURRENT_RELATIONS_RELATED_PARTY_LIST_TAG, CURRENT_RELATIONS_RELATED_PARTY_TAG]

# ---------------------------------------
#             OTHER LIABILITIES
# ---------------------------------------

    OTHER_LIABILITIES_TAG = "OtherLiabilities"
    OTHER_LIABILIITY_LIST_TAG = "OtherLiabilityList"
    OTHER_LIABILITY_TAG = "OtherLiability"
    OTHER_LIABILITIES_SUMMARY_TAG = "Summary"
    
    OTHER_LIABILITIES_ROOT = [OTHER_LIABILITIES_TAG, OTHER_LIABILIITY_LIST_TAG, OTHER_LIABILITY_TAG]
    OTHER_LIABILITIES_SUMMARY_ROOT = [OTHER_LIABILITIES_TAG, OTHER_LIABILITIES_SUMMARY_TAG]

# ---------------------------------------
#             DISPUTES
# --------------------------------------- 
    
    DISPUTES_TAG = 'Disputes'
    DISPUTE_SUMMARY_TAG = 'Summary'

    DISPUTES_ROOT = [DISPUTES_TAG, DISPUTE_SUMMARY_TAG]

# ---------------------------------------
#             DASHBOARD
# ---------------------------------------

    DASHBOARD_TAG = "Dashboard"
    DASHBOARD_CIQ_TAG = "CIQ"
    DASHBOARD_COLLATERALS_TAG = "Collaterals"
    DASHBOARD_DISPUTES_TAG = "Disputes"
    DASHBOARD_INQUIRIES_TAG = 'Inquiries'
    DASHBOARD_INVOLVEMENTS_TAG = 'Involvements'
    DASHBOARD_OTHER_LIABILITIES_TAG = 'OtherLiabilities'
    DASHBOARD_PAYMENTS_PROFILE_TAG = 'PaymentsProfile'
    DASHBOARD_RELATIONS_TAG = 'Relations'
    DASHBOARD_SECURITIES_TAG = 'Securities'
    
    DASHBOARD_CIQ_ROOT = [DASHBOARD_TAG, DASHBOARD_CIQ_TAG]
    DASHBOARD_COLLATERALS_ROOT = [DASHBOARD_TAG, DASHBOARD_COLLATERALS_TAG]
    DASHBOARD_DISPUTES_ROOT = [DASHBOARD_TAG, DASHBOARD_DISPUTES_TAG]
    DASHBOARD_INQUIRIES_ROOT = [DASHBOARD_TAG, DASHBOARD_INQUIRIES_TAG]
    DASHBOARD_INVOLVEMENTS_ROOT = [DASHBOARD_TAG, DASHBOARD_INVOLVEMENTS_TAG]
    DASHBOARD_OTHER_LIABILITIES_ROOT = [DASHBOARD_TAG, DASHBOARD_OTHER_LIABILITIES_TAG]
    DASHBOARD_PAYMENTS_PROFILE_ROOT = [DASHBOARD_TAG, DASHBOARD_PAYMENTS_PROFILE_TAG]
    DASHBOARD_RELATIONS_ROOT = [DASHBOARD_TAG, DASHBOARD_RELATIONS_TAG]
    DASHBOARD_SECURITIES_ROOT = [DASHBOARD_TAG, DASHBOARD_SECURITIES_TAG]


# The fields of the XML document
    VALUE = "Value"
    LOCAL_VALUE = "LocalValue"
    CURRENCY = "Currency"
    CONTACT_VALUE = 'MobilePhone'
    ADDRESS_VALUE = 'PostalCode'

    INDIVIDUAL_ADDRESS = ['AddressLine', 'City', 'Country', 'District', 'Parish', 'PostalCode', 'Street']
    INDIVIDUAL_CONTACT = ['MobilePhone', 'FixedLine']

    FIELD_ADDRESS = [
        'MainAddress'
    ]

    FIELD_CONTACT = [
        'Contact',
    ]

    FIELD_INT = [
        "AppraisalValue",
        "BankValue",
        "CollateralValue",
        "ContractsSubmitted",
        "HighestCollateralValue",
        "InitialTotalAmount",
        "InterestRate",
        "InterestArrears",
        "InterestArrearsFrequency",
        "NumberOfActiveSecurities",
        "NumberOfClosedAgreements",
        "NumberOfOpenAgreements",
        "NumberOfPastSecurities",
        "NumberOfCancelledClosedContracts",
        "NumberOfCollaterals",
        "NumberOfFraudAlertsPrimarySubject",
        "NumberOfFraudAlertsThirdParty",
        "NumberOfInquiriesLast12Months",
        "NumberOfInquiriesLast1Month",
        "NumberOfInquiriesLast24Months",
        "NumberOfInquiriesLast3Months",
        "NumberOfInquiriesLast6Months",
        "NumberOfSubscribersMadeInquiriesLast14Days",
        "NumberOfSubscribersMadeInquiriesLast2Days",
        "OutstandingAmount",
        "PastDueAmount",
        "PastDueDays",
        "PastDueInterest",
        "Penalty",
        "PrincipalArrears",
        "PrincipalBalance",
        "ProbabilityOfDefault",
        "Score",
        "SubscribersInLast12Months",
        "TotalAmount",
        "TotalCollateralValue",
        "TotalFacilityAmount",
        "TotalTakenAmount",
        "WorstPastDueAmount",
        "WorstPastDueDays"
    ]

    # FIELD_INT = ["Score",
    #              "ProbabilityOfDefault",
    #              "NumberOfCancelledClosedContracts",
    #              "NumberOfSubscribersMadeInquiriesLast14Days",
    #              "NumberOfSubscribersMadeInquiriesLast2Days",
    #              "NumberOfFraudAlertsPrimarySubject",
    #              "NumberOfFraudAlertsThirdParty",
    #              "InitialTotalAmount",
    #              "InterestArrears",
    #              "InterestArrearsFrequency",
    #              "OutstandingAmount",
    #              "PastDueAmount",
    #              "PastDueDays",
    #              "PastDueInterest",
    #              "Penalty",
    #              "PrincipalArrears",
    #              "PrincipalBalance",
    #              "TotalAmount",
    #              "TotalFacilityAmount",
    #              "TotalTakenAmount",
    #              "WorstPastDueAmount",
    #              "WorstPastDueDays",
    #              "HighestCollateralValue",
    #              "TotalCollateralValue",
    #              "NumberOfCollaterals",
    #              "BankValue",
    #              "CollateralValue",
    #              "AppraisalValue",
    #              "SubscribersInLast12Months",
    #              "NumberOfInquiriesLast1Month",
    #              "NumberOfInquiriesLast3Months",
    #              "NumberOfInquiriesLast6Months",
    #              "NumberOfInquiriesLast12Months",
    #              "NumberOfInquiriesLast24Months"
    #              ]
    FIELD_DATE = ['Date']

    FIELD_AMOUNT = ["OutstandingAmount",
                    "PastDueAmount",
                    "PastDueInterest",
                    "InitialTotalAmount",
                    "InterestArrears",
                    "Penalty",
                    "PrincipalArrears",
                    "PrincipalBalance",
                    "TotalAmount",
                    "TotalFacilityAmount",
                    "TotalTakenAmount",
                    "WorstPastDueAmount",
                    "BankValue",
                    "CollateralValue",
                    "AppraisalValue",
                    "TotalAmountOfActiveInvolvements",
                    "TotalMarketValue",
                    "TotalPrincipalArrears",
                    "TotalNonCashCollateralValue",
                    "OutstandingAmountSum",
                    "PastDueAmountSum",
                    "TotalAmountSum",
                    "DebtorOutstandingAmountSum",
                    "DebtorPastDueAmountSum",
                    "DebtorTotalAmountSum",
                    "GuarantorOutstandingAmountSum",
                    "GuarantorPastDueAmountSum",
                    "GuarantorTotalAmountSum"
                    ]    
    # FIELD_AMOUNT = ["OutstandingAmount",
    #                 "PastDueAmount",
    #                 "PastDueInterest",
    #                 "InitialTotalAmount",
    #                 "InterestArrears",
    #                 "Penalty",
    #                 "PrincipalArrears",
    #                 "PrincipalBalance",
    #                 "TotalAmount",
    #                 "TotalFacilityAmount",
    #                 "TotalTakenAmount",
    #                 "WorstPastDueAmount",
    #                 "BankValue",
    #                 "CollateralValue",
    #                 "AppraisalValue"
    #                 ]
    CIP = ["Date", "Grade", "ProbabilityOfDefault", "Score", "Trend"]
    CIP_REASON_KEY = ["Date"]
    CIP_REASON = ["Code", "Description"]
    CIQ_DETAIL = ["NumberOfCancelledClosedContracts",
                  "NumberOfSubscribersMadeInquiriesLast14Days",
                  "NumberOfSubscribersMadeInquiriesLast2Days"]
    CIQ_SUMMARY = ["DateOfLastFraudRegistrationPrimarySubject",
                   "DateOfLastFraudRegistrationThirdParty",
                   "NumberOfFraudAlertsPrimarySubject",
                   "NumberOfFraudAlertsThirdParty"
                   ]
    DEBTOR = ["ClosedContracts", "OpenContracts", "OutstandingAmountSum", "PastDueAmountSum", "TotalAmountSum"]
    GUARANTOR = ["ClosedContracts", "OpenContracts", "OutstandingAmountSum", "PastDueAmountSum", "TotalAmountSum"]
    CONTRACT_SUMMARY_OVERALL = ["LastDelinquency90PlusDays", 
                                "WorstPastDueAmount",
                                "WorstPastDueDays",]

    CONTRACT_CORE_KEY = ["ContractCode","Creditor"]
    CONTRACT = ["ContractStatus",
                "ConditionDate",
                "ContractCode",
                "ContractCurrency",
                "ContractType",
                "CreditClassification",
                # "CreditUsageInLast30Days",
                "Creditor",
                "CreditorType",
                # "CollateralsList",
                "DefaultDate",
                "DefaultReasonDescription",
                "DefaultReason",
                "DelinquencyDate",
                "DisbursementDate",
                # "Disputes",
                "EconomicSector",
                "InitialAgreementDate",
                "InitialAgreementNumber",
                "InitialInterestRate",
                "InitialInterestRateType",
                "InitialTotalAmount",
                "InterestArrears",
                "InterestArrearsFrequency",
                "LastAgreementDate",
                "LastAgreementNumber",
                "LastDelinquency90PlusDays",
                "LastInterestRate",
                "LastInterestRateType",
                "LastUpdate",
                "MaturityDate",
                "NameOfInsured",
                "NegativeStatusOfContract",
                "OutstandingAmount",
                "PastDueAmount",
                "PastDueDays",
                "PastDueInterest",
                # "PaymentCalendarList",
                "Penalty",
                "PhaseOfContract",
                "PrincipalArrears",
                "PrincipalArrearsFrequency",
                "PrincipalBalance",
                "PurposeOfFinancing",
                "RealEndDate",
                "RestructuringDate",
                "RoleOfClient",
                "StartDate",
                "SyndicatedLoan",
                "TotalAmount",
                "TotalFacilityAmount",
                "TotalTakenAmount",
                "WorstPastDueAmount",
                "WorstPastDueDays",
                "Description"
                ]
    
    CONTRACT_COLLATERAL = ["AppraisalValue",
                           "BankValuationDate",
                           "BankValue",
                           "Branch",
                           "CollateralAcceptanceDate",
                           "CollateralAppraisalAuthority",
                           "CollateralCode",
                           "CollateralDescription",
                           "CollateralOwnerName",
                           "CollateralRating",
                           "CollateralStatus",
                           "CollateralType",
                           "CollateralValue",
                           "HasMultipleCollaterals",
                           "Insurance",
                           "IsShared",
                           "MainAddressAddressLine",
                           "MainAddressCity",
                           "MainAddressStreet",
                           "ProofOfOwnership",
                           "RatingAuthority",
                           "SecurityAssignmentType",
                           "SharedPortion",
                           "ValuationDate"
                           ]

    PARAMETER = ["Consent",
                 "IDNumber",
                 "IDNumberType",
                 "InquiryReason",
                 "ReportDate",
                 "SubjectType"
                 ]
    
    SECURITIES = ["NumberOfActiveSecurities",
                "NumberOfPastSecurities",
                "TotalMarketValue",
                "TotalPrincipalArrears",
    ]
    
    OTHER_LIABILITIES = ["Branch",
                         "ConditionDate",
                         "ContractCode",
                         "ContractStatus",
                         "ContractType",
                         "Creditor",
                         "CurrencyOfContract",
                         "DefaultDate",
                         "DefaultReason",
                         "DefaultReasonDescription",
                         "DelinquencyDate",
                         "Description",
                         "InitialTotalAmount",
                         "InterestRate",
                         "IssueDate",
                         "LastUpdate",
                         "MarketValue",
                         "MaturityDate",
                         "NegativeStatus",
                         "OutstandingAmount",
                         "PastDueDays",
                         "PreviousContractCode",
                         "PrincipalArrears",
                         "Rating",
                         "RealEndDate"
                         ]
    
    OTHER_LIABILITIES_SUMMARY = ["NumberOfClosedAgreements",
                                "NumberOfOpenAgreements",
                                "TotalMarketValue",
                                "TotalPrincipalArrears"
                         ]

    INDIVIDUAL_CONTACT = ["FixedLine", "MobilePhone"]
    INDIVIDUAL_GENERAL = ["Alias",
                          "Citizenship",
                          "ClassificationOfIndividual",
                          "DateOfBirth",
                          "Education",
                          "EmployerName",
                          "EmployerSector",
                          "Employment",
                          "FullName",
                          "Gender",
                          "MotherMaidenName",
                          "PlaceOfBirth",
                          "SocialStatus"
                          ]
    INDIVIDUAL_IDENTIFICATION = ["KTP", "NPWP", "PassportIssuerCountry", "PassportNumber"]
    INDIVIDUAL_PEFINDO_ID = ["PefindoId"] # version 553
    # INDIVIDUAL_PEFINDO_ID = ["IdScoreId"] # version 58
    
    INDIVIDUAL_ADDRESS = ["AddressLine", "City", "Country", "District", "Parish", "PostalCode", "Street"]

    INQUIRIES = [
        "DateOfInquiry",
        "Product",
        "Reason",
        "Sector",
        "SubscriberInfo"
    ]

    INQUIRIES_SUMMARY = [
        "NumberOfInquiriesLast1Month",
        "NumberOfInquiriesLast3Months",
        "NumberOfInquiriesLast6Months",
        "NumberOfInquiriesLast12Months",
        "NumberOfInquiriesLast24Months"
    ]

    REPORTINFO = [
        "Created",
        "ReferenceNumber",
        "ReportStatus",
        "RequestedBy",
        "Version"
    ]

    SUBJECTINFO_LIST = []

    SUBJECTINFO = [
        "Item",
        "Subscriber",
        "ValidFrom",
        "ValidTo",
        "Value"
    ]

    CONTRACTRELATIONS = [
        "FullName",
        "IDNumber",
        "IDNumberType",
        "IdScoreId",
        "RoleOfCustomer",
        "SubjectType",
        "ValidFrom",
        "Contact",
        "MainAddress"
    ]

    RELATEDPARTY = [
        "FullName",
        "Gender",
        "IDNumber",
        "IDNumberType",
        "IdScoreId",
        "LTV",
        "OwnershipShare",
        "SubjectStatus",
        "SubjectType",
        "TypeOfRelation",
        "ValidFrom",
        "Contact",
        "MainAddress"
    ]

    CONTACT = [
        "FixedLine",
        "MobilePhone"
    ]

    INVOLVEMENTS_SUMMARY = ["NumberOfActiveInvolvements",
                            "NumberOfPastInvolvements",
                            "TotalAmountOfActiveInvolvements"]

    CONTRACT_OVERVIEW = ["ContractCode","Creditor","ContractStatus",
                         "OutstandingAmount",
                         "PastDueAmount",
                         "PastDueDays",
                         "PhaseOfContract",
                         "RoleOfClient",
                         "Sector",
                         "StartDate",
                         "TotalAmount",
                         "TypeOfContract"
                         ]
    DISPUTE = ["NumberOfActiveDisputesContracts",
               "NumberOfActiveDisputesInCourt",
               "NumberOfActiveDisputesSubjectData",
               "NumberOfClosedDisputesContracts",
               "NumberOfClosedDisputesSubjectData",
               "NumberOfFalseDisputes"
               ]
    SECTORINFO = ["DebtorClosedContracts",
                  "DebtorOpenContracts",
                  "DebtorOutstandingAmountSum",
                  "DebtorPastDueAmountSum",
                  "DebtorTotalAmountSum",
                  "GuarantorClosedContracts",
                  "GuarantorOpenContracts",
                  "GuarantorOutstandingAmountSum",
                  "GuarantorPastDueAmountSum",
                  "GuarantorTotalAmountSum",
                  "Sector"
                  ]
    COLLATERALS = ["HighestCollateralValue",
                   "HighestCollateralValueType",
                   "NumberOfCollaterals",
                   "TotalCollateralValue"]
    
    CALENDARITEM = ['Date',
                    'DelinquencyStatus',
                    'InterestRate',
                    'NegativeStatusOfContract',
                    'OutstandingAmount',
                    'PastDueAmount',
                    'PastDueDays']
    
    PAYMENTCALENDAR = ["ContractsSubmitted",
                       "Date",
                       "NegativeStatusOfContract",
                       "OutstandingAmount",
                       "PastDueAmount",
                       "PastDueDays"]
    
    DASHBOARD_CIQ = ["FraudAlerts",
                 "FraudAlertsThirdParty"]
    
    DASHBOARD_COLLATERALS = ["NumberOfCollaterals",
                             "TotalNonCashCollateralValue"]

    DASHBOARD_DISPUTES = ["ActiveContractDisputes",
                          "FalseDisputes",
                          "NumberOfCourtRegisteredDisputes"]
    
    DASHBOARD_INQUIRIES = ["InquiriesForLast12Months",
                    "SubscribersInLast12Months"]
    DASHBOARD_INVOLVEMENTS = ["NumberOfActiveInvolvements"]
    DASHBOARD_OTHER_LIABILITIES = ["NumberOfOpenAgreements"]
    DASHBOARD_PAYMENTS_PROFILE = ["ClosedContracts",
                                  "NumberOfDifferentSubscribers",
                                  "OpenContracts",
                                  "PastDueAmountSum",
                                  "WorstPastDueDaysCurrent",
                                  "WorstPastDueDaysForLast12Months"]
    
    DASHBOARD_RELATIONS = ["NumberOfInvolvements",
                           "NumberOfRelations",
                           ]
    
    DASHBOARD_SECURITIES = ["NumberOfActiveSecurities",]
    
    INQUIRY = ["Reason",
               "Sector"]
