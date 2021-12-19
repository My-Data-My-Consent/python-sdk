"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import com.mydatamyconsent
from com.mydatamyconsent.model.application_user import ApplicationUser
from com.mydatamyconsent.model.country import Country
from com.mydatamyconsent.model.document_provider_category import DocumentProviderCategory
from com.mydatamyconsent.model.organization_address import OrganizationAddress
from com.mydatamyconsent.model.organization_category import OrganizationCategory
from com.mydatamyconsent.model.organization_financial_account import OrganizationFinancialAccount
from com.mydatamyconsent.model.organization_kyo_document import OrganizationKyoDocument
from com.mydatamyconsent.model.organization_meta_data import OrganizationMetaData
from com.mydatamyconsent.model.organization_status import OrganizationStatus
from com.mydatamyconsent.model.organization_type import OrganizationType
globals()['ApplicationUser'] = ApplicationUser
globals()['Country'] = Country
globals()['DocumentProviderCategory'] = DocumentProviderCategory
globals()['OrganizationAddress'] = OrganizationAddress
globals()['OrganizationCategory'] = OrganizationCategory
globals()['OrganizationFinancialAccount'] = OrganizationFinancialAccount
globals()['OrganizationKyoDocument'] = OrganizationKyoDocument
globals()['OrganizationMetaData'] = OrganizationMetaData
globals()['OrganizationStatus'] = OrganizationStatus
globals()['OrganizationType'] = OrganizationType
from com.mydatamyconsent.model.organization import Organization


class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganization(self):
        """Test Organization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Organization()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
