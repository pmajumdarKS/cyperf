# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.simulated_id_p import SimulatedIdP

class TestSimulatedIdP(unittest.TestCase):
    """SimulatedIdP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimulatedIdP:
        """Test SimulatedIdP
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimulatedIdP`
        """
        model = SimulatedIdP()
        if include_optional:
            return SimulatedIdP(
                assertion_signature = True,
                audience_uri = '',
                cert_config = cyperf.models.cert_config.CertConfig(
                    certificate_file = null, 
                    dh_file = null, 
                    get_sni_conflicts = [
                        'YQ=='
                        ], 
                    id = '', 
                    is_playlist = True, 
                    key_file = null, 
                    key_file_password = '', 
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
                    playlist_column_name = '', 
                    playlist_filename = '', 
                    resolve_sni_conflicts = [
                        cyperf.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    sni_hostname = '', ),
                name_id_format = 'emailAddress',
                response_signature = True,
                signature_algorithm = 'SHA256_SIGN',
                single_sign_on_url = '',
                xml_metadata = [
                    'YQ=='
                    ],
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
                    ]
            )
        else:
            return SimulatedIdP(
                assertion_signature = True,
                audience_uri = '',
                name_id_format = 'emailAddress',
                response_signature = True,
                single_sign_on_url = '',
        )
        """

    def testSimulatedIdP(self):
        """Test SimulatedIdP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
