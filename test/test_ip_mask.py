# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ip_mask import IpMask

class TestIpMask(unittest.TestCase):
    """IpMask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpMask:
        """Test IpMask
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpMask`
        """
        model = IpMask()
        if include_optional:
            return IpMask(
                ip = '',
                net_mask = 56
            )
        else:
            return IpMask(
        )
        """

    def testIpMask(self):
        """Test IpMask"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
