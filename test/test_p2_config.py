# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.p2_config import P2Config

class TestP2Config(unittest.TestCase):
    """P2Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> P2Config:
        """Test P2Config
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `P2Config`
        """
        model = P2Config()
        if include_optional:
            return P2Config(
                enc_algorithm = 'NONE',
                hash_algorithm = 'HMAC MD5 96',
                lifetime = 56,
                nat_enabled = True,
                pfs_enabled = True,
                pfs_group = 'MODP 768'
            )
        else:
            return P2Config(
                enc_algorithm = 'NONE',
                hash_algorithm = 'HMAC MD5 96',
                lifetime = 56,
                nat_enabled = True,
                pfs_enabled = True,
                pfs_group = 'MODP 768',
        )
        """

    def testP2Config(self):
        """Test P2Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
