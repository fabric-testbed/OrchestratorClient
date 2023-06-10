# coding: utf-8

"""
    Fabric Orchestrator API

    This is Fabric Orchestrator API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.poas_api import PoasApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPoasApi(unittest.TestCase):
    """PoasApi unit test stubs"""

    def setUp(self):
        self.api = PoasApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_poas_create_sliver_id_post(self):
        """Test case for poas_create_sliver_id_post

        Perform an operational action on a sliver.  # noqa: E501
        """
        pass

    def test_poas_get(self):
        """Test case for poas_get

        Request get the status of the POAs.  # noqa: E501
        """
        pass

    def test_poas_poa_id_get(self):
        """Test case for poas_poa_id_get

        Perform an operational action on a sliver.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
