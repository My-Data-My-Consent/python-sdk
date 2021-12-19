"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.mydatamyconsent
from com.mydatamyconsent.api.data_processing_agreements_api import DataProcessingAgreementsApi  # noqa: E501


class TestDataProcessingAgreementsApi(unittest.TestCase):
    """DataProcessingAgreementsApi unit test stubs"""

    def setUp(self):
        self.api = DataProcessingAgreementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_data_agreements_get(self):
        """Test case for v1_data_agreements_get

        Get all data processing agreements.  # noqa: E501
        """
        pass

    def test_v1_data_agreements_id_delete(self):
        """Test case for v1_data_agreements_id_delete

        Delete a data processing agreement. This will not delete a published or a agreement in use with consents.  # noqa: E501
        """
        pass

    def test_v1_data_agreements_id_get(self):
        """Test case for v1_data_agreements_id_get

        Get data processing agreement by Id.  # noqa: E501
        """
        pass

    def test_v1_data_agreements_id_put(self):
        """Test case for v1_data_agreements_id_put

        Update a data processing agreement.  # noqa: E501
        """
        pass

    def test_v1_data_agreements_id_terminate_put(self):
        """Test case for v1_data_agreements_id_terminate_put

        Terminate a data processing agreement.  # noqa: E501
        """
        pass

    def test_v1_data_agreements_post(self):
        """Test case for v1_data_agreements_post

        Create a data processing agreement.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
