# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.attack_track import AttackTrack

class TestAttackTrack(unittest.TestCase):
    """AttackTrack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttackTrack:
        """Test AttackTrack
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttackTrack`
        """
        model = AttackTrack()
        if include_optional:
            return AttackTrack(
                actions = [
                    null
                    ],
                add_actions = [
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
                    ]
            )
        else:
            return AttackTrack(
                id = '',
        )
        """

    def testAttackTrack(self):
        """Test AttackTrack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
