# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from mydatamyconsent.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from mydatamyconsent.model.activity import Activity
from mydatamyconsent.model.approved_consent_request import ApprovedConsentRequest
from mydatamyconsent.model.bank_account_type import BankAccountType
from mydatamyconsent.model.collectible_types import CollectibleTypes
from mydatamyconsent.model.consent_template_types import ConsentTemplateTypes
from mydatamyconsent.model.create_data_processing_agreement_request_model import CreateDataProcessingAgreementRequestModel
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from mydatamyconsent.model.data_consent_identifier import DataConsentIdentifier
from mydatamyconsent.model.data_consent_request import DataConsentRequest
from mydatamyconsent.model.data_consent_request_model import DataConsentRequestModel
from mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
from mydatamyconsent.model.data_consent_requested_financial_account import DataConsentRequestedFinancialAccount
from mydatamyconsent.model.data_consent_requester_dto import DataConsentRequesterDto
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from mydatamyconsent.model.data_processing_agreement_dto_paginated_list import DataProcessingAgreementDtoPaginatedList
from mydatamyconsent.model.data_protection_officer import DataProtectionOfficer
from mydatamyconsent.model.data_provider import DataProvider
from mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from mydatamyconsent.model.digital_signature import DigitalSignature
from mydatamyconsent.model.document import Document
from mydatamyconsent.model.document_category_type import DocumentCategoryType
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from mydatamyconsent.model.documents_required import DocumentsRequired
from mydatamyconsent.model.fetch_types import FetchTypes
from mydatamyconsent.model.file_type import FileType
from mydatamyconsent.model.financial import Financial
from mydatamyconsent.model.financial_account import FinancialAccount
from mydatamyconsent.model.financial_account_details_required import FinancialAccountDetailsRequired
from mydatamyconsent.model.financial_accounts import FinancialAccounts
from mydatamyconsent.model.get_consent_template_details_dto import GetConsentTemplateDetailsDto
from mydatamyconsent.model.identification_strategy import IdentificationStrategy
from mydatamyconsent.model.identifier import Identifier
from mydatamyconsent.model.identifier_string_key_value_pair import IdentifierStringKeyValuePair
from mydatamyconsent.model.identity_supported_fields import IdentitySupportedFields
from mydatamyconsent.model.life import Life
from mydatamyconsent.model.organization_data_consent_info_dto import OrganizationDataConsentInfoDto
from mydatamyconsent.model.organization_data_consent_info_dto_paginated_list import OrganizationDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.organization_document_details_dto import OrganizationDocumentDetailsDto
from mydatamyconsent.model.organization_document_download_dto import OrganizationDocumentDownloadDto
from mydatamyconsent.model.organization_financial_account_dto import OrganizationFinancialAccountDto
from mydatamyconsent.model.organization_financial_transactions_dto import OrganizationFinancialTransactionsDto
from mydatamyconsent.model.organization_financial_transactions_dto_paginated_list import OrganizationFinancialTransactionsDtoPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.push_uri_request import PushUriRequest
from mydatamyconsent.model.push_uri_response import PushUriResponse
from mydatamyconsent.model.receiver import Receiver
from mydatamyconsent.model.receiver_type import ReceiverType
from mydatamyconsent.model.shared_with import SharedWith
from mydatamyconsent.model.update_data_processing_agreement_request_model import UpdateDataProcessingAgreementRequestModel
from mydatamyconsent.model.uri_details import UriDetails
from mydatamyconsent.model.user_account_financial_transactions_dto import UserAccountFinancialTransactionsDto
from mydatamyconsent.model.user_account_financial_transactions_dto_paginated_list import UserAccountFinancialTransactionsDtoPaginatedList
from mydatamyconsent.model.user_data_consent_info_dto import UserDataConsentInfoDto
from mydatamyconsent.model.user_data_consent_info_dto_paginated_list import UserDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.user_document_details_dto import UserDocumentDetailsDto
from mydatamyconsent.model.user_document_download_dto import UserDocumentDownloadDto
