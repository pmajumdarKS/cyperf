# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_v2_disk_usage_get200_response_one_of import ApiV2DiskUsageGet200ResponseOneOf

class TestApiV2DiskUsageGet200ResponseOneOf(unittest.TestCase):
    """ApiV2DiskUsageGet200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2DiskUsageGet200ResponseOneOf:
        """Test ApiV2DiskUsageGet200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2DiskUsageGet200ResponseOneOf`
        """
        model = ApiV2DiskUsageGet200ResponseOneOf()
        if include_optional:
            return ApiV2DiskUsageGet200ResponseOneOf(
                data = openapi_client.models.disk_usage.DiskUsage(
                    available = 56, 
                    consumers = [
                        openapi_client.models.consumer.Consumer(
                            id = '', 
                            pretty_size = '', 
                            size = 56, )
                        ], 
                    critical_disk_space = True, 
                    low_disk_space = True, 
                    message = '', 
                    pretty_available = '', 
                    pretty_size = '', 
                    size = 56, ),
                total_count = 56
            )
        else:
            return ApiV2DiskUsageGet200ResponseOneOf(
        )
        """

    def testApiV2DiskUsageGet200ResponseOneOf(self):
        """Test ApiV2DiskUsageGet200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
