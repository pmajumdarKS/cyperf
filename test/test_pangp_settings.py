# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pangp_settings import PANGPSettings

class TestPANGPSettings(unittest.TestCase):
    """PANGPSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PANGPSettings:
        """Test PANGPSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PANGPSettings`
        """
        model = PANGPSettings()
        if include_optional:
            return PANGPSettings(
                var_auth_settings = openapi_client.models.auth_settings.AuthSettings(
                    auth_method = null, 
                    auth_param = null, 
                    certificate_file = null, 
                    key_file = null, 
                    key_file_password = '', 
                    passwords = [
                        ''
                        ], 
                    passwords_param = null, 
                    usernames = [
                        ''
                        ], 
                    usernames_param = null, ),
                outer_tcp_profile = openapi_client.models.tcp_profile.TcpProfile(
                    close_with_reset = True, 
                    defer_accept = True, 
                    ecn_enabled = True, 
                    max_rto = 56, 
                    max_src_port = 56, 
                    min_rto = 56, 
                    min_src_port = 56, 
                    ping_pong = True, 
                    pmtu_disc_disabled = True, 
                    recycle_tw_enabled = True, 
                    reordering = True, 
                    reuse_tw_enabled = True, 
                    rx_buffer = 56, 
                    sack_enabled = True, 
                    sock_group = '', 
                    timestamp_hdr_enabled = True, 
                    tx_buffer = 56, 
                    user_mss = 56, 
                    wscale_enabled = True, ),
                esp_probe_retry_timeout = 56,
                esp_probe_timeout = 56,
                is_portal = True,
                outer_tls_client_profile = openapi_client.models.tls_profile.TLSProfile(
                    certificate_file = null, 
                    cipher = null, 
                    cipher12 = null, 
                    cipher13 = null, 
                    ciphers12 = [
                        'ECDHE-RSA-AES256-GCM-SHA384'
                        ], 
                    ciphers13 = [
                        'AES-256-GCM-SHA384'
                        ], 
                    dh_file = null, 
                    get_tls_conflicts = [
                        'YQ=='
                        ], 
                    immediate_close = True, 
                    key_file = null, 
                    key_file_password = '', 
                    middle_box_enabled = True, 
                    profile_id = '', 
                    resolve_tls_conflicts = [
                        openapi_client.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    send_close_notify = True, 
                    session_reuse_count = 56, 
                    session_reuse_method = null, 
                    session_reuse_method12 = null, 
                    session_reuse_method13 = null, 
                    sni_cert_configs = [
                        openapi_client.models.cert_config.CertConfig(
                            certificate_file = null, 
                            dh_file = null, 
                            id = '', 
                            is_playlist = True, 
                            key_file = null, 
                            key_file_password = '', 
                            playlist_column_name = '', 
                            playlist_filename = '', 
                            sni_hostname = '', )
                        ], 
                    sni_enabled = True, 
                    tls12_enabled = True, 
                    tls13_enabled = True, 
                    use_tls_profile = True, 
                    version = 'NONE', ),
                pangp_encapsulation = openapi_client.models.pangp_encapsulation.PANGPEncapsulation(
                    esp_over_udp_enabled = True, 
                    esp_over_udp_settings = null, 
                    encapsulation_mode = 'ESP_OVER_UDP', 
                    udp_port = 56, ),
                portal_hostname = '02::84',
                vpn_gateway = '',
                vpn_gateways = [
                    ''
                    ]
            )
        else:
            return PANGPSettings(
                var_auth_settings = openapi_client.models.auth_settings.AuthSettings(
                    auth_method = null, 
                    auth_param = null, 
                    certificate_file = null, 
                    key_file = null, 
                    key_file_password = '', 
                    passwords = [
                        ''
                        ], 
                    passwords_param = null, 
                    usernames = [
                        ''
                        ], 
                    usernames_param = null, ),
                outer_tcp_profile = openapi_client.models.tcp_profile.TcpProfile(
                    close_with_reset = True, 
                    defer_accept = True, 
                    ecn_enabled = True, 
                    max_rto = 56, 
                    max_src_port = 56, 
                    min_rto = 56, 
                    min_src_port = 56, 
                    ping_pong = True, 
                    pmtu_disc_disabled = True, 
                    recycle_tw_enabled = True, 
                    reordering = True, 
                    reuse_tw_enabled = True, 
                    rx_buffer = 56, 
                    sack_enabled = True, 
                    sock_group = '', 
                    timestamp_hdr_enabled = True, 
                    tx_buffer = 56, 
                    user_mss = 56, 
                    wscale_enabled = True, ),
                outer_tls_client_profile = openapi_client.models.tls_profile.TLSProfile(
                    certificate_file = null, 
                    cipher = null, 
                    cipher12 = null, 
                    cipher13 = null, 
                    ciphers12 = [
                        'ECDHE-RSA-AES256-GCM-SHA384'
                        ], 
                    ciphers13 = [
                        'AES-256-GCM-SHA384'
                        ], 
                    dh_file = null, 
                    get_tls_conflicts = [
                        'YQ=='
                        ], 
                    immediate_close = True, 
                    key_file = null, 
                    key_file_password = '', 
                    middle_box_enabled = True, 
                    profile_id = '', 
                    resolve_tls_conflicts = [
                        openapi_client.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    send_close_notify = True, 
                    session_reuse_count = 56, 
                    session_reuse_method = null, 
                    session_reuse_method12 = null, 
                    session_reuse_method13 = null, 
                    sni_cert_configs = [
                        openapi_client.models.cert_config.CertConfig(
                            certificate_file = null, 
                            dh_file = null, 
                            id = '', 
                            is_playlist = True, 
                            key_file = null, 
                            key_file_password = '', 
                            playlist_column_name = '', 
                            playlist_filename = '', 
                            sni_hostname = '', )
                        ], 
                    sni_enabled = True, 
                    tls12_enabled = True, 
                    tls13_enabled = True, 
                    use_tls_profile = True, 
                    version = 'NONE', ),
                pangp_encapsulation = openapi_client.models.pangp_encapsulation.PANGPEncapsulation(
                    esp_over_udp_enabled = True, 
                    esp_over_udp_settings = null, 
                    encapsulation_mode = 'ESP_OVER_UDP', 
                    udp_port = 56, ),
                portal_hostname = '02::84',
                vpn_gateway = '',
                vpn_gateways = [
                    ''
                    ],
        )
        """

    def testPANGPSettings(self):
        """Test PANGPSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
