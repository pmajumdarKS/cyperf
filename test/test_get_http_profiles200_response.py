# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_http_profiles200_response import GetHttpProfiles200Response

class TestGetHttpProfiles200Response(unittest.TestCase):
    """GetHttpProfiles200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetHttpProfiles200Response:
        """Test GetHttpProfiles200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHttpProfiles200Response`
        """
        model = GetHttpProfiles200Response()
        if include_optional:
            return GetHttpProfiles200Response(
                data = [
                    cyperf.models.http_profile.HTTPProfile(
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
                            cyperf.models.params.Params(
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
                                enum = cyperf.models.params_enum.Params_Enum(
                                    choices = [
                                        cyperf.models.choice.Choice(
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
                                    cyperf.models.media_file.MediaFile(
                                        file_value = null, 
                                        media_tracks = [
                                            cyperf.models.media_track.MediaTrack(
                                                bitrate = 56, 
                                                bitrate_kbps = 56, 
                                                codec = '', 
                                                codec_description = '', 
                                                track_id = '', 
                                                track_type = null, 
                                                id = '', )
                                            ], 
                                        id = '', 
                                        links = [
                                            cyperf.models.api_link.APILink(
                                                content_type = '', 
                                                href = '', 
                                                id = '', 
                                                method = '', 
                                                name = '', 
                                                references_count = 56, 
                                                rel = 'self', 
                                                type = 'self', )
                                            ], )
                                    ], 
                                metadata = cyperf.models.param_metadata.ParamMetadata(
                                    type_info = cyperf.models.param_metadata_type_info.ParamMetadata_TypeInfo(
                                        array_v2 = cyperf.models.param_metadata_type_info_array_v2.ParamMetadata_TypeInfo_arrayV2(
                                            elements = [
                                                cyperf.models.param_metadata_type_info_array_v2_elements_inner.ParamMetadata_TypeInfo_arrayV2_elements_inner(
                                                    id = '', )
                                                ], ), 
                                        int = cyperf.models.param_metadata_type_info_int.ParamMetadata_TypeInfo_int(
                                            max_value = 56, 
                                            min_value = 56, ), 
                                        media = cyperf.models.param_metadata_type_info_media.ParamMetadata_TypeInfo_media(
                                            track_id = '', 
                                            track_type = '', ), 
                                        string = cyperf.models.param_metadata_type_info_string.ParamMetadata_TypeInfo_string(
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
                                links = [
                                    cyperf.models.api_link.APILink(
                                        content_type = '', 
                                        href = '', 
                                        id = '', 
                                        method = '', 
                                        name = '', 
                                        references_count = 56, 
                                        rel = 'self', 
                                        type = 'self', )
                                    ], 
                                supports_dynamic_payload = True, 
                                upload_url = '', )
                            ], 
                        use_application_server_headers = True, 
                        links = , )
                    ],
                total_count = 56
            )
        else:
            return GetHttpProfiles200Response(
        )
        """

    def testGetHttpProfiles200Response(self):
        """Test GetHttpProfiles200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
