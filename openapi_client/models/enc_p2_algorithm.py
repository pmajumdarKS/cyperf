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


class EncP2Algorithm(str, Enum):
    """
    EncP2Algorithm
    """

    """
    allowed enum values
    """
    NONE = 'NONE'
    AES128_CBC = 'AES128 CBC'
    AES192_CBC = 'AES192 CBC'
    AES256_CBC = 'AES256 CBC'
    AES128_GCM_ICV8 = 'AES128 GCM ICV8'
    AES192_GCM_ICV8 = 'AES192 GCM ICV8'
    AES256_GCM_ICV8 = 'AES256 GCM ICV8'
    AES128_GCM_ICV12 = 'AES128 GCM ICV12'
    AES192_GCM_ICV12 = 'AES192 GCM ICV12'
    AES256_GCM_ICV12 = 'AES256 GCM ICV12'
    AES128_GCM_ICV16 = 'AES128 GCM ICV16'
    AES192_GCM_ICV16 = 'AES192 GCM ICV16'
    AES256_GCM_ICV16 = 'AES256 GCM ICV16'
    ENC_MINUS_NONE = 'ENC-NONE'
    PH2_MINUS_AES128_MINUS_CBC = 'PH2-AES128-CBC'
    PH2_MINUS_AES192_MINUS_CBC = 'PH2-AES192-CBC'
    PH2_MINUS_AES256_MINUS_CBC = 'PH2-AES256-CBC'
    PH2_MINUS_AES128_MINUS_GCM_MINUS_ICV_MINUS_8 = 'PH2-AES128-GCM-ICV-8'
    PH2_MINUS_AES192_MINUS_GCM_MINUS_ICV_MINUS_8 = 'PH2-AES192-GCM-ICV-8'
    PH2_MINUS_AES256_MINUS_GCM_MINUS_ICV_MINUS_8 = 'PH2-AES256-GCM-ICV-8'
    PH2_MINUS_AES128_MINUS_GCM_MINUS_ICV_MINUS_12 = 'PH2-AES128-GCM-ICV-12'
    PH2_MINUS_AES192_MINUS_GCM_MINUS_ICV_MINUS_12 = 'PH2-AES192-GCM-ICV-12'
    PH2_MINUS_AES256_MINUS_GCM_MINUS_ICV_MINUS_12 = 'PH2-AES256-GCM-ICV-12'
    PH2_MINUS_AES128_MINUS_GCM_MINUS_ICV_MINUS_16 = 'PH2-AES128-GCM-ICV-16'
    PH2_MINUS_AES192_MINUS_GCM_MINUS_ICV_MINUS_16 = 'PH2-AES192-GCM-ICV-16'
    PH2_MINUS_AES256_MINUS_GCM_MINUS_ICV_MINUS_16 = 'PH2-AES256-GCM-ICV-16'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EncP2Algorithm from a JSON string"""
        return cls(json.loads(json_str))


