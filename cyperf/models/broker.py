# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Broker(BaseModel):
    """
    Broker
    """ # noqa: E501
    connection_status: Optional[StrictStr] = Field(default=None, description="The broker's connection status", alias="connectionStatus")
    fingerprint: Optional[StrictStr] = Field(default=None, description="The broker's fingerprint")
    host: Optional[StrictStr] = Field(default=None, description="The IP or hostname of the registered broker")
    host_name: Optional[StrictStr] = Field(default=None, description="The IP or hostname of the registered broker", alias="hostName")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the broker")
    interactive_fingerprint_verification: Optional[StrictBool] = Field(default=None, description="Validate the broker's fingerprint interactively", alias="interactiveFingerprintVerification")
    password: Optional[StrictStr] = Field(default=None, description="The broker's authentication password")
    pretty_conn_status: Optional[StrictStr] = Field(default=None, description="The broker's connection status in human readable format", alias="prettyConnStatus")
    trust_new: Optional[StrictBool] = Field(default=None, description="The flag used to skip broker's identity verifications", alias="trustNew")
    user: Optional[StrictStr] = Field(default=None, description="The broker's authentication user")
    __properties: ClassVar[List[str]] = ["connectionStatus", "fingerprint", "host", "hostName", "id", "interactiveFingerprintVerification", "password", "prettyConnStatus", "trustNew", "user"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Broker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "host",
            "host_name",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Broker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "connectionStatus": obj.get("connectionStatus"),
                        "fingerprint": obj.get("fingerprint"),
                        "host": obj.get("host"),
                        "hostName": obj.get("hostName"),
                        "id": obj.get("id"),
                        "interactiveFingerprintVerification": obj.get("interactiveFingerprintVerification"),
                        "password": obj.get("password"),
                        "prettyConnStatus": obj.get("prettyConnStatus"),
                        "trustNew": obj.get("trustNew"),
                        "user": obj.get("user")
            ,
            "links": obj.get("links")
        })
        return _obj


