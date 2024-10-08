# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_attacks200_response_one_of import GetAttacks200ResponseOneOf

class TestGetAttacks200ResponseOneOf(unittest.TestCase):
    """GetAttacks200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAttacks200ResponseOneOf:
        """Test GetAttacks200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAttacks200ResponseOneOf`
        """
        model = GetAttacks200ResponseOneOf()
        if include_optional:
            return GetAttacks200ResponseOneOf(
                data = [
                    cyperf.models.appsec_attack.AppsecAttack(
                        attack = null, 
                        description = '', 
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
                        name = '', 
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
                        owner = '', 
                        owner_id = '', )
                    ],
                total_count = 56
            )
        else:
            return GetAttacks200ResponseOneOf(
        )
        """

    def testGetAttacks200ResponseOneOf(self):
        """Test GetAttacks200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
