# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.config_metadata import ConfigMetadata

class TestConfigMetadata(unittest.TestCase):
    """ConfigMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigMetadata:
        """Test ConfigMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigMetadata`
        """
        model = ConfigMetadata()
        if include_optional:
            return ConfigMetadata(
                application = '',
                config_data = {
                    'key' : null
                    },
                config_url = '',
                created_on = 56,
                display_name = '',
                encoded_files = True,
                id = '',
                last_accessed = 56,
                last_modified = 56,
                linked_resources = [
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
                owner = '',
                owner_id = '',
                readonly = True,
                tags = {
                    'key' : ''
                    },
                type = '',
                version = openapi_client.models.version.Version(
                    config_service_version = '', 
                    data_model_version = '', )
            )
        else:
            return ConfigMetadata(
        )
        """

    def testConfigMetadata(self):
        """Test ConfigMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
