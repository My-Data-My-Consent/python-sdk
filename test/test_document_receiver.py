"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import mydatamyconsent
from mydatamyconsent.model.identification_strategy import IdentificationStrategy
from mydatamyconsent.model.string_string_key_value_pair import StringStringKeyValuePair
globals()['IdentificationStrategy'] = IdentificationStrategy
globals()['StringStringKeyValuePair'] = StringStringKeyValuePair
from mydatamyconsent.model.document_receiver import DocumentReceiver


class TestDocumentReceiver(unittest.TestCase):
    """DocumentReceiver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDocumentReceiver(self):
        """Test DocumentReceiver"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DocumentReceiver()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
