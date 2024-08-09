# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.type_string_metadata import TypeStringMetadata

class TestTypeStringMetadata(unittest.TestCase):
    """TypeStringMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TypeStringMetadata:
        """Test TypeStringMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TypeStringMetadata`
        """
        model = TypeStringMetadata()
        if include_optional:
            return TypeStringMetadata(
                charset = '',
                max_length = 56,
                min_length = 56
            )
        else:
            return TypeStringMetadata(
        )
        """

    def testTypeStringMetadata(self):
        """Test TypeStringMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
