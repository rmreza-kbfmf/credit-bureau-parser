class PefindoFeatures():
# ---------------------------------------
# Main root of the JSON document
# ---------------------------------------

# Main root of the XML document
    ROOT = ["data"]
    REPORT_ROOT = 'report'
# ---------------------------------------
#                  CIP 
# ---------------------------------------
# CIP in JSON covered in SCORING

    CIP_TAG = "scoring"
    CIP_RECORDLIST_TAG = "RecordList"
    CIP_RECORD_TAG = "Record"
    CIP_REASONSLIST_TAG = "ReasonsList"
    CIP_REASON_TAG = "Reason"

    CIP_ROOT = [CIP_TAG]
    # CIP_REASON_ROOT = [CIP_REASONSLIST_TAG, CIP_REASON_TAG]


# ---------------------------------------
#                DEBITUR
# ---------------------------------------
    
    INDIVIDUAL_TAG = "debitur"

    INDIVIDUAL_ROOT=[REPORT_ROOT, INDIVIDUAL_TAG]

    INDIVIDUAL_CONTACT_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]
    INDIVIDUAL_GENERAL_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]
    INDIVIDUAL_IDENTIFICATION_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]
    INDIVIDUAL_ADDRESS_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]

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

# ---------------------------------------
#             DISPUTES
# --------------------------------------- 
    
    DISPUTES_TAG = 'Disputes'
    DISPUTE_SUMMARY_TAG = 'Summary'

    DISPUTES_ROOT = [DISPUTES_TAG, DISPUTE_SUMMARY_TAG]


# ---------------------------------------
#                FASILITAS
# ---------------------------------------

    CONTRACTS_TAG = "fasilitas"
    CONTRACT_PAYMENT_CALENDAR_TAG = "riwayat_fasilitas"
    CONTRACTS_ROOT = [REPORT_ROOT, CONTRACTS_TAG]

# ---------------------------------------
#              COLLARETAL
# ---------------------------------------

    COLLATERAL_TAG = "agunan"

    COLLATERAL_ROOT = [COLLATERAL_TAG]



# ---------------------------------------
#              REPORT INFO
# ---------------------------------------

    REPORT_INFO_TAG = "ReportInfo"

    REPORT_INFO_ROOT = [REPORT_INFO_TAG]

# ---------------------------------------
#               SECURITIES
# ---------------------------------------

    SECURITIES_TAG = "Securities"
    SECURITIES_SUMMARY_TAG = "Summary"
    
    SECURITIES_SUMMARY_ROOT = [SECURITIES_TAG, SECURITIES_SUMMARY_TAG]


# ---------------------------------------
#                FASILITAS OVERVIEW
# ---------------------------------------

    CONTRACT_OVERVIEW_ROOT = [REPORT_ROOT, CONTRACTS_TAG]

# ---------------------------------------
#              INVOLVEMENTS
# ---------------------------------------

    INVOLVEMENTS_TAG = "Involvements"
    INVOLVEMENTS_SUMMARY_TAG = "Summary"

    INVOLVEMENTS_SUMMARY_ROOT = [INVOLVEMENTS_TAG, INVOLVEMENTS_SUMMARY_TAG]


# ---------------------------------------
#              INQUIRIES / PERMINTAAN DATA
# ---------------------------------------

    INQUIRIES_TAG = "permintaan_data"
    INQUIRIES_SUMMARY_TAG = "summary_permintaan_data"


    INQUIRIES_SUMMARY_ROOT = [REPORT_ROOT, INQUIRIES_SUMMARY_TAG]
    INQUIRIES_INQUIRYLIST_ROOT = [REPORT_ROOT, INQUIRIES_TAG]


# ---------------------------------------
#                CONTRACT SUMMARY
# ---------------------------------------
    SUMMARY_RIWAYAT_TAG='summary_riwayat_debitur'

    CONTRACT_SUMMARY_DEBTOR_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]

    CONTRACT_SUMMARY_GUARANTOR_ROOT = [REPORT_ROOT, SUMMARY_RIWAYAT_TAG]

    CONTRACT_SUMMARY_OVERALL_ROOT = [REPORT_ROOT, INDIVIDUAL_TAG]
    CONTRACT_SUMMARY_PAYMENT_CALENDAR_ROOT = [REPORT_ROOT, SUMMARY_RIWAYAT_TAG]

# ---------------------------------------
#         PAYMENT CALENDAR
# ---------------------------------------

    CALENDAR_TAG = "riwayat_fasilitas"

    PAYMENT_CALENDAR_ROOT = [CALENDAR_TAG]

    CALENDARITEM = ['tahun_bulan_data',
                    'status_tunggakan',
                    'suku_bunga_atau_imbalan',
                    'id_kolektabilitas',
                    'saldo_terutang',
                    'nominal_tunggakan',
                    'jumlah_hari_tunggakan']

# ---------------------------------------
#               PARAMETERS
# ---------------------------------------

    PARAMETERS_TAG = "header"
    
    PARAMETERS_ROOT = [REPORT_ROOT, PARAMETERS_TAG]

# ---------------------------------------
#          CURRENT RELATIONS
# ---------------------------------------

    CURRENT_RELATIONS_TAG = "CurrentRelations"
    CURRENT_RELATIONS_CONTRACT_RELATION_LIST_TAG = "ContractRelationList"

    CURRENT_RELATIONS_RELATED_PARTY_TAG = "pengurus"
    CURRENT_RELATIONS_CONTRACT_RELATION_TAG = "ContractRelation"
    CURRENT_RELATIONS_CONTACT_TAG = "Contact"
    CURRENT_RELATIONS_MAIN_ADDRESS_TAG = "Address"
    
    CURRENT_RELATIONS_CONTRACT_RELATION_ROOT = [CURRENT_RELATIONS_TAG, CURRENT_RELATIONS_CONTRACT_RELATION_LIST_TAG, CURRENT_RELATIONS_CONTRACT_RELATION_TAG]
    CURRENT_RELATIONS_CONTACT_TAG_ROOT = [CURRENT_RELATIONS_CONTRACT_RELATION_ROOT, CURRENT_RELATIONS_CONTACT_TAG]
    CURRENT_RELATIONS_MAIN_ADDRESS_TAG_ROOT = [CURRENT_RELATIONS_CONTRACT_RELATION_ROOT, CURRENT_RELATIONS_MAIN_ADDRESS_TAG]
    CURRENT_RELATIONS_RELATED_PARTY_ROOT = [CURRENT_RELATIONS_RELATED_PARTY_TAG]


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
#          SUBJECT INFO HISTORY
# ---------------------------------------

    SUBJECT_INFO_HISTORY_TAG='riwayat_identitas_debitur'

    # RIWAYAT_IDENTITAS_ROOT=[REPORT_TAG,DEBITUR_TAG,RIWAYAT_IDENTITAS_TAG]
    SUBJECT_INFO_LIST_ROOT = [REPORT_ROOT, SUBJECT_INFO_HISTORY_TAG]

    SUBJECT_INFO_ADDRESS_LIST_ROOT = []
    SUBJECT_INFO_CONTACT_LIST_ROOT = []
    SUBJECT_INFO_GENERAL_LIST_ROOT = []
    SUBJECT_INFO_IDENTIFICATION_LIST_ROOT = []



# The fields of the JSON document  (Belum....)
    FIELD_INT = [
        "nilai_agunan_menurut_penilai_independen",
        "nilai_agunan_menurut_pelapor",
        "nilai_agunan_sesuai_njop",
        "nilai_dalam_mata_uang_asal",
        "suku_bunga_atau_imbalan",
        "jml_permintaan_12bln",
        "saldo_terutang",
        "nominal_tunggakan",
        "jumlah_hari_tunggakan",
        "tunggakan_bunga_atau_imbalan",
        "denda",
        "tunggakan_pokok",
        "baki_debet",
        "pod",
        "score",
        "jml_pelapor_12bln",
        "plafon",
        "plafon_awal",
        "realisasi_atau_pencairan_bulan_berjalan",
        "tunggakan_terburuk",
        "jml_hari_tunggakan_terburuk"
    ]

    FIELD_ADDRESS = [
        'MainAddress'
    ]

    FIELD_CONTACT = [
        'Contact'
    ]
    
    FIELD_AMOUNT = ["saldo_terutang",
                    "nominal_tunggakan",
                    "tunggakan_bunga_atau_imbalan",
                    "nilai_dalam_mata_uang_asal",
                    "denda",
                    "tunggakan_pokok",
                    "baki_debet",
                    "plafon",
                    "plafon_awal",
                    "realisasi_atau_pencairan_bulan_berjalan",
                    "tunggakan_terburuk",
                    "nilai_agunan_menurut_pelapor",
                    "nilai_agunan_sesuai_njop",
                    "nilai_agunan_menurut_penilai_independen",
                    "jml_nilai_agunan"
                    ] 

    FIELD_DATE = ["tgl_permintaan"]     

    CIP = ["period", "risk_grade", "pod", "score"]
    CIP_REASON_KEY = ["period"]
    CIP_REASON = ["period","reason_code", "reason_desc"]

    INDIVIDUAL_PEFINDO_ID = ["id_debitur_golden_record"]

    INDIVIDUAL_CONTACT = ["telepon", "telepon_seluler"]
    INDIVIDUAL_ADDRESS = ["alamat_debitur", "id_kabupaten_kota","kecamatan", "kelurahan"]
    INDIVIDUAL_GENERAL = [
                          "id_pekerjaan",
                          "tanggal_lahir",
                          "id_status_gelar",
                          "tempat_bekerja",
                          "id_sektor_ekonomi",
                          "nama_sesuai_identitas",
                          "id_jenis_kelamin",
                          "nama_gadis_ibu_kandung",
                          "tempat_lahir",
                          ]
    INDIVIDUAL_IDENTIFICATION = ["nomor_identitas", "npwp", "id_negara"]

    CONTRACT_CORE_KEY = ["nomor_rekening_fasilitas","id_pelapor"]
    CONTRACT = ["id_kondisi",
                "tanggal_kondisi",
                "nomor_rekening_fasilitas",
                "id_valuta",
                "id_jenis_kredit",
                "id_pelapor",
                "id_jenis_pelapor",
                "tanggal_macet",
                "keterangan_sebab_macet",
                "id_sebab_macet",
                "disbursement_date",
                "id_sektor_ekonomi",
                "tanggal_akad_awal",
                "nomor_akad_awal",
                "nilai_dalam_mata_uang_asal",
                "tanggal_akad_akhir",
                "nomor_akad_akhir",
                "tgl_tunggakan_terakhir",
                "suku_bunga_atau_imbalan",
                "id_jenis_suku_bunga_atau_imbalan",
                "tahun_bulan_data",
                "tanggal_jatuh_tempo",
                "id_kolektabilitas",
                "saldo_terutang",
                "nominal_tunggakan",
                "jumlah_hari_tunggakan",
                "tunggakan_bunga_atau_imbalan",
                "denda",
                "fase_fasilitas",
                "tunggakan_pokok",
                "frekuensi_tunggakan",
                "baki_debet",
                "id_jenis_penggunaan",
                "tanggal_akhir",
                "tanggal_restrukturisasi_akhir",
                "tanggal_awal_kredit_atau_pembiayaan",
                "plafon",
                "plafon_awal",
                "realisasi_atau_pencairan_bulan_berjalan",
                "tunggakan_terburuk",
                "jml_hari_tunggakan_terburuk",
                "keterangan"
                ]

    INVOLVEMENTS_SUMMARY = ["NumberOfActiveInvolvements",
                            "NumberOfPastInvolvements",
                            "TotalAmountOfActiveInvolvements"]
    
    CONTRACT_OVERVIEW = ["id_kondisi",
                        "saldo_terutang",
                        "nominal_tunggakan",
                        "jumlah_hari_tunggakan",
                        "fase_fasilitas",
                         "tanggal_awal_kredit_atau_pembiayaan",
                         "plafon",
                         "id_jenis_kredit"
                         ]    

    CONTRACT_COLLATERAL = [
                "nilai_agunan_menurut_penilai_independen",
                "tanggal_penilaian_agunan_menurut_pelapor",
                "nilai_agunan_menurut_pelapor",
                "id_kantor_cabang",
                "tanggal_pengikatan",
                "nama_penilai_independen",
                "kode_register_atau_nomor_agunan",
                "keterangan",
                "nama_pemilik_agunan",
                "peringkat_agunan",
                "id_status_agunan",
                "id_jenis_agunan",
                "nilai_agunan_sesuai_njop",
                "diasuransikan",
                "status_paripasu",
                "alamat_agunan",
                "id_kabupaten_kota",
                "bukti_kepemilikan",
                "id_lembaga_pemeringkat",
                "id_jenis_pengikatan",
                "persentase_paripasu",
                "tanggal_penilaian_agunan_menurut_penilai_independen"
                ]

    PARAMETER = ["tgl_permintaan",
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

    DISPUTE = ["NumberOfActiveDisputesContracts",
               "NumberOfActiveDisputesInCourt",
               "NumberOfActiveDisputesSubjectData",
               "NumberOfClosedDisputesContracts",
               "NumberOfClosedDisputesSubjectData",
               "NumberOfFalseDisputes"
               ]

    DEBTOR = ["jml_tutup_fasilitas", "jml_aktif_fasilitas", "jml_saldo_terutang", "jml_tunggakan", "jml_plafon"]

    GUARANTOR = ["jml_tutup_fasilitas", "jml_aktif_fasilitas", "jml_saldo_terutang", "jml_tunggakan", "jml_plafon"]

    CONTRACT_SUMMARY_OVERALL = ["tgl_tunggakan_terakhir",
                                "tunggakan_terburuk",
                                "jml_hari_tunggakan_terburuk"]

    INQUIRIES = [
        "tgl_permintaan",
        "id_tujuan_permintaan",
        "deskripsi_jenis_ljk",
        "id_jenis_pelapor"
    ]

    INQUIRIES_SUMMARY = [
        "jml_permintaan_12bln"
    ]

    PAYMENTCALENDAR = ["tahun_bulan_data",
                       "kolektabilitas_terburuk",
                       "status_tunggakan",
                       "jml_hari_tunggakan_terburuk"]
    
    RELATEDPARTY = [
        "nama_pengurus_dan_atau_pemilik_debitur_badan_usaha",
        "id_jenis_kelamin",
        "nomor_identitas_pengurus_dan_atau_pemilik_debitur_badan_usaha",
        "id_jenis_identitas",
        "pangsa_kepemilikan",
        "status_pengurus_dan_atau_pemilik_debitur_badan_usaha",
        "id_tipe_debitur",
        "id_jabatan",
        "tahun_bulan_data",
        "alamat",
        "id_kabupaten_kota",
        "kecamatan",
        "kelurahan"
    ]    

    SUBJECTINFO_LIST = [
        "id_elemen",
        "id_pelapor",
        "tahun_bulan_data",
        "value"
    ]

    SUBJECTINFO = []  

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

    REPORTINFO = [
        "Created",
        "ReferenceNumber",
        "ReportStatus",
        "RequestedBy",
        "Version"
    ]

    LOCAL_VALUE = "LocalValue"