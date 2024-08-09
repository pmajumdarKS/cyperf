# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tunnel_range import TunnelRange

class TestTunnelRange(unittest.TestCase):
    """TunnelRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TunnelRange:
        """Test TunnelRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TunnelRange`
        """
        model = TunnelRange()
        if include_optional:
            return TunnelRange(
                cisco_any_connect_settings = None,
                dcp_request_timeout = 56,
                dns_resolver = openapi_client.models.dns_resolver.DNSResolver(
                    cache_timeout = 56, 
                    enable_perconnect = True, 
                    name_servers = [
                        openapi_client.models.name_server.NameServer(
                            name = '4.207.188.200', )
                        ], ),
                f5_settings = None,
                fortinet_settings = None,
                pangp_settings = None,
                tcp_dst_port = 56,
                tunnel_count_per_outer_ip = 56,
                tunnel_establishment_timeout = 56,
                vendor_type = 'CISCO_ANY_CONNECT'
            )
        else:
            return TunnelRange(
                cisco_any_connect_settings = None,
                dcp_request_timeout = 56,
                f5_settings = None,
                fortinet_settings = None,
                pangp_settings = None,
                tcp_dst_port = 56,
                tunnel_count_per_outer_ip = 56,
                vendor_type = 'CISCO_ANY_CONNECT',
        )
        """

    def testTunnelRange(self):
        """Test TunnelRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
