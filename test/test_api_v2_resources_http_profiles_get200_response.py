# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_v2_resources_http_profiles_get200_response import ApiV2ResourcesHttpProfilesGet200Response

class TestApiV2ResourcesHttpProfilesGet200Response(unittest.TestCase):
    """ApiV2ResourcesHttpProfilesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2ResourcesHttpProfilesGet200Response:
        """Test ApiV2ResourcesHttpProfilesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2ResourcesHttpProfilesGet200Response`
        """
        model = ApiV2ResourcesHttpProfilesGet200Response()
        if include_optional:
            return ApiV2ResourcesHttpProfilesGet200Response(
                data = [
                    openapi_client.models.http_profile.HTTPProfile(
                        additional_headers = null, 
                        connection_persistence = null, 
                        connections_max_transactions = 56, 
                        description = '', 
                        external_resource_url = '', 
                        http_version = null, 
                        headers = null, 
                        is_modified = True, 
                        name = '', 
                        params = [
                            openapi_client.models.params.Params(
                                array_element_type = '', 
                                array_elements = [
                                    {
                                        'key' : ''
                                        }
                                    ], 
                                category = '', 
                                category_index = 56, 
                                deprecated_previous_source = '', 
                                description = '', 
                                dictionary_value = {
                                    'key' : ''
                                    }, 
                                enum = openapi_client.models.params_enum.Params_Enum(
                                    choices = [
                                        openapi_client.models.choice.Choice(
                                            description = '', 
                                            hidden = True, 
                                            name = '', 
                                            value = '', )
                                        ], ), 
                                file_value = null, 
                                flow_identifier = True, 
                                is_deprecated = True, 
                                is_modified = True, 
                                media_files = [
                                    openapi_client.models.media_file.MediaFile(
                                        file_value = null, 
                                        media_tracks = [
                                            openapi_client.models.media_track.MediaTrack(
                                                bitrate = 56, 
                                                bitrate_kbps = 56, 
                                                codec = '', 
                                                codec_description = '', 
                                                track_id = '', 
                                                track_type = null, 
                                                id = '', )
                                            ], 
                                        id = '', )
                                    ], 
                                metadata = openapi_client.models.param_metadata.ParamMetadata(
                                    type_info = openapi_client.models.param_metadata_type_info.ParamMetadata_TypeInfo(
                                        array_v2 = openapi_client.models.param_metadata_type_info_array_v2.ParamMetadata_TypeInfo_arrayV2(
                                            elements = [
                                                openapi_client.models.param_metadata_type_info_array_v2_elements_inner.ParamMetadata_TypeInfo_arrayV2_elements_inner(
                                                    id = '', 
                                                    type = '', )
                                                ], ), 
                                        int = openapi_client.models.param_metadata_type_info_int.ParamMetadata_TypeInfo_int(
                                            max_value = 56, 
                                            min_value = 56, ), 
                                        media = openapi_client.models.param_metadata_type_info_media.ParamMetadata_TypeInfo_media(
                                            track_id = '', 
                                            track_type = '', ), 
                                        string = openapi_client.models.param_metadata_type_info_string.ParamMetadata_TypeInfo_string(
                                            charset = '', 
                                            max_length = 56, 
                                            min_length = 56, ), ), ), 
                                name = '', 
                                param_id = '', 
                                readonly = True, 
                                source = '', 
                                supported_sources = [
                                    ''
                                    ], 
                                type = '', 
                                value = '', 
                                file_upload = [
                                    'YQ=='
                                    ], 
                                id = '', 
                                supports_dynamic_payload = True, 
                                upload_url = '', )
                            ], 
                        use_application_server_headers = True, )
                    ],
                total_count = 56
            )
        else:
            return ApiV2ResourcesHttpProfilesGet200Response(
        )
        """

    def testApiV2ResourcesHttpProfilesGet200Response(self):
        """Test ApiV2ResourcesHttpProfilesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
