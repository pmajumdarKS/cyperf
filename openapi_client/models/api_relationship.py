# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class APIRelationship(str, Enum):
    """
    Defines possible relationships for APILinks.
    """

    """
    allowed enum values
    """
    SELF = 'self'
    META = 'meta'
    CHILD = 'child'
    DOC = 'doc'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of APIRelationship from a JSON string"""
        return cls(json.loads(json_str))


