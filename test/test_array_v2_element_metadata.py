# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.array_v2_element_metadata import ArrayV2ElementMetadata

class TestArrayV2ElementMetadata(unittest.TestCase):
    """ArrayV2ElementMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayV2ElementMetadata:
        """Test ArrayV2ElementMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayV2ElementMetadata`
        """
        model = ArrayV2ElementMetadata()
        if include_optional:
            return ArrayV2ElementMetadata(
                id = '',
                type = ''
            )
        else:
            return ArrayV2ElementMetadata(
        )
        """

    def testArrayV2ElementMetadata(self):
        """Test ArrayV2ElementMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
