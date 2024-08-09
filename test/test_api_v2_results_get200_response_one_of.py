# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_v2_results_get200_response_one_of import ApiV2ResultsGet200ResponseOneOf

class TestApiV2ResultsGet200ResponseOneOf(unittest.TestCase):
    """ApiV2ResultsGet200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2ResultsGet200ResponseOneOf:
        """Test ApiV2ResultsGet200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2ResultsGet200ResponseOneOf`
        """
        model = ApiV2ResultsGet200ResponseOneOf()
        if include_optional:
            return ApiV2ResultsGet200ResponseOneOf(
                data = [
                    openapi_client.models.result_metadata.ResultMetadata(
                        active_session = '', 
                        config_url = '', 
                        csv_url = '', 
                        display_name = '', 
                        download_all = null, 
                        download_diagnostic = null, 
                        end_time = 56, 
                        files = [
                            openapi_client.models.result_file_metadata.ResultFileMetadata(
                                file_id = '', 
                                file_name = '', 
                                id = '', 
                                last_modified = 56, 
                                result_id = '', 
                                type = '', )
                            ], 
                        id = '', 
                        last_modified = 56, 
                        marked_as_deleted = openapi_client.models.marked_as_deleted.MarkedAsDeleted(
                            delete_progress = 56, 
                            value = True, ), 
                        owner = '', 
                        owner_id = '', 
                        pdf_url = '', 
                        pinned = True, 
                        reporting_links = [
                            openapi_client.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                id = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = 'self', 
                                type = 'self', )
                            ], 
                        result_url = '', 
                        start_time = 56, 
                        tags = {
                            'key' : ''
                            }, 
                        test_name = '', 
                        type = '', 
                        user_tags = [
                            ''
                            ], )
                    ],
                total_count = 56
            )
        else:
            return ApiV2ResultsGet200ResponseOneOf(
        )
        """

    def testApiV2ResultsGet200ResponseOneOf(self):
        """Test ApiV2ResultsGet200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
