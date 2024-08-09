# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.error_description import ErrorDescription

class TestErrorDescription(unittest.TestCase):
    """ErrorDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorDescription:
        """Test ErrorDescription
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorDescription`
        """
        model = ErrorDescription()
        if include_optional:
            return ErrorDescription(
                error = ''
            )
        else:
            return ErrorDescription(
                error = '',
        )
        """

    def testErrorDescription(self):
        """Test ErrorDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
