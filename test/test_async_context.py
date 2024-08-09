# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.async_context import AsyncContext

class TestAsyncContext(unittest.TestCase):
    """AsyncContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncContext:
        """Test AsyncContext
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncContext`
        """
        model = AsyncContext()
        if include_optional:
            return AsyncContext(
                id = 56,
                message = '',
                progress = 56,
                result = None,
                result_url = '',
                state = '',
                type = '',
                url = ''
            )
        else:
            return AsyncContext(
        )
        """

    def testAsyncContext(self):
        """Test AsyncContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
