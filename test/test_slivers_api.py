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

from fabric_cf.orchestrator.swagger_client.api.slivers_api import SliversApi  # noqa: E501
from fabric_cf.orchestrator.swagger_client.rest import ApiException


class TestSliversApi(unittest.TestCase):
    """SliversApi unit test stubs"""

    def setUp(self):
        self.api = SliversApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_slivers_get(self):
        """Test case for slivers_get

        Retrieve a listing of user slivers  # noqa: E501
        """
        pass

    def test_slivers_sliver_id_get(self):
        """Test case for slivers_sliver_id_get

        slivers properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
