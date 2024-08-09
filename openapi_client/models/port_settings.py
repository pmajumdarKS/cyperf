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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.effective_ports import EffectivePorts
from typing import Optional, Set
from typing_extensions import Self

class PortSettings(BaseModel):
    """
    PortSettings
    """ # noqa: E501
    automatic: StrictBool = Field(alias="Automatic")
    automatic_destination_port: StrictBool = Field(alias="AutomaticDestinationPort")
    automatic_forward_proxy_port: StrictBool = Field(alias="AutomaticForwardProxyPort")
    destination_port: StrictInt = Field(alias="DestinationPort")
    effective_ports: Optional[EffectivePorts] = Field(default=None, alias="EffectivePorts")
    forward_proxy_port: StrictInt = Field(alias="ForwardProxyPort")
    readonly: StrictBool = Field(description="If true, the port can't be selected by the user", alias="Readonly")
    server_listen_port: StrictInt = Field(alias="ServerListenPort")
    __properties: ClassVar[List[str]] = ["Automatic", "AutomaticDestinationPort", "AutomaticForwardProxyPort", "DestinationPort", "EffectivePorts", "ForwardProxyPort", "Readonly", "ServerListenPort"]

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
        """Create an instance of PortSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of effective_ports
        if self.effective_ports:
            _dict['EffectivePorts'] = self.effective_ports.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Automatic": obj.get("Automatic"),
            "AutomaticDestinationPort": obj.get("AutomaticDestinationPort"),
            "AutomaticForwardProxyPort": obj.get("AutomaticForwardProxyPort"),
            "DestinationPort": obj.get("DestinationPort"),
            "EffectivePorts": EffectivePorts.from_dict(obj["EffectivePorts"]) if obj.get("EffectivePorts") is not None else None,
            "ForwardProxyPort": obj.get("ForwardProxyPort"),
            "Readonly": obj.get("Readonly"),
            "ServerListenPort": obj.get("ServerListenPort")
        })
        return _obj


