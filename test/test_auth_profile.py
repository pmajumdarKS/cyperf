# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.auth_profile import AuthProfile

class TestAuthProfile(unittest.TestCase):
    """AuthProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthProfile:
        """Test AuthProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthProfile`
        """
        model = AuthProfile()
        if include_optional:
            return AuthProfile(
                connections = [
                    cyperf.models.connection.Connection(
                        client_endpoint = '', 
                        client_port = 56, 
                        closing_end = '', 
                        disable_encryption = True, 
                        hostname = '', 
                        hostname_param = null, 
                        http_forward_proxy_mode = 'INHERIT_DUT', 
                        is_deprecated = True, 
                        max_transactions = 56, 
                        name = '', 
                        port_settings = null, 
                        readonly = True, 
                        readonly_hostname = True, 
                        readonly_max_trans = True, 
                        readonly_type = True, 
                        server_endpoint = '', 
                        server_port = 56, 
                        type = 'http', 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = 'self', 
                                type = 'self', )
                            ], )
                    ],
                data_types = [
                    cyperf.models.data_type.DataType(
                        values = [
                            cyperf.models.data_type_values_inner.DataType_Values_inner(
                                id = '', 
                                value_type = '', )
                            ], 
                        id = '', )
                    ],
                endpoints = [
                    cyperf.models.endpoint.Endpoint(
                        name = '', 
                        network_mapping = null, 
                        type = 'Client', 
                        id = '', 
                        links = [
                            cyperf.models.api_link.APILink(
                                content_type = '', 
                                href = '', 
                                method = '', 
                                name = '', 
                                references_count = 56, 
                                rel = 'self', 
                                type = 'self', )
                            ], )
                    ],
                file_name = '',
                metadata = cyperf.models.metadata.Metadata(
                    direction = '', 
                    is_banner = True, 
                    keywords = [
                        null
                        ], 
                    legacy_names = [
                        ''
                        ], 
                    protocol = '', 
                    rtp_profile_meta = cyperf.models.rtp_profile_meta.RTPProfileMeta(
                        custom_header_len_offset = 56, 
                        custom_header_len_size = 56, 
                        custom_header_signature = 'YQ==', 
                        custom_header_signature_offset = 56, 
                        custom_header_size = 56, 
                        encryption_mode = '', 
                        requires_rtp_profile = True, ), 
                    references = [
                        cyperf.models.reference.Reference(
                            type = '', 
                            value = '', )
                        ], 
                    requires_uniqueness = True, 
                    severity = '', 
                    skip_attack_generation = True, 
                    sort_severity = '', 
                    static = True, 
                    supported_apps = [
                        ''
                        ], 
                    year = '', ),
                parameters = [
                    cyperf.models.parameter.Parameter(
                        default_array_elements = [
                            {
                                'key' : ''
                                }
                            ], 
                        default_source = '', 
                        default_value = '', 
                        element_type = '', 
                        metadata = cyperf.models.parameter_metadata.ParameterMetadata(
                            category = '', 
                            category_index = 56, 
                            default = '', 
                            description = '', 
                            display_name = '', 
                            enum = cyperf.models.enum.Enum(
                                choices = [
                                    cyperf.models.choice.Choice(
                                        description = '', 
                                        hidden = True, 
                                        name = '', 
                                        value = '', )
                                    ], 
                                default = '', ), 
                            flow_identifier = True, 
                            input = '', 
                            legacy_names = [
                                ''
                                ], 
                            mandatory = True, 
                            payload = cyperf.models.payload_metadata.PayloadMetadata(
                                file_extension = '', 
                                file_name = '', 
                                file_type = '', 
                                file_url = '', ), 
                            readonly = True, 
                            shared = True, 
                            type = '', 
                            type_info = cyperf.models.type_info_metadata.TypeInfoMetadata(
                                array_v2 = cyperf.models.type_array_v2_metadata.TypeArrayV2Metadata(
                                    elements = [
                                        cyperf.models.array_v2_element_metadata.ArrayV2ElementMetadata(
                                            id = '', 
                                            type = '', )
                                        ], ), 
                                int = cyperf.models.type_int_metadata.TypeIntMetadata(
                                    max_value = 56, 
                                    min_value = 56, ), 
                                media = cyperf.models.type_media_metadata.TypeMediaMetadata(
                                    track_id = '', 
                                    track_type = '', ), 
                                string = cyperf.models.type_string_metadata.TypeStringMetadata(
                                    charset = '', 
                                    max_length = 56, 
                                    min_length = 56, ), ), 
                            unique_value = True, 
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
                                ], ), 
                        sources = [
                            ''
                            ], 
                        type = '', 
                        field = '', 
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
                        operator = '', 
                        query_param = '', )
                    ],
                description = '',
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
                type = ''
            )
        else:
            return AuthProfile(
        )
        """

    def testAuthProfile(self):
        """Test AuthProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
