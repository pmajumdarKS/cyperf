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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.api_link import APILink
from cyperf.models.http_profile import HTTPProfile
from cyperf.models.rtp_profile import RTPProfile
from cyperf.models.tcp_profile import TcpProfile
from cyperf.models.tls_profile import TLSProfile
from cyperf.models.udp_profile import UdpProfile
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class TransportProfile(BaseModel):
    """
    TransportProfile
    """ # noqa: E501
    client_http_profile: Optional[HTTPProfile] = Field(default=None, description="The client HTTP profile used in the Scenario.", alias="ClientHTTPProfile")
    client_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ClientTLSProfile")
    client_tcp_profile: Optional[TcpProfile] = Field(default=None, alias="ClientTcpProfile")
    ip_tos: Optional[StrictInt] = Field(default=None, alias="IpTos")
    rtp_profile: Optional[RTPProfile] = Field(default=None, alias="RTPProfile")
    server_http_profile: Optional[HTTPProfile] = Field(default=None, description="The server HTTP profile used in the Scenario.", alias="ServerHTTPProfile")
    server_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ServerTLSProfile")
    server_tcp_profile: Optional[TcpProfile] = Field(default=None, alias="ServerTcpProfile")
    udp_profile: Optional[UdpProfile] = Field(default=None, alias="UdpProfile")
    vlan_prio: Optional[StrictInt] = Field(default=None, alias="VlanPrio")
    links: Optional[List[APILink]] = None
    l4_profile_name: StrictStr = Field(alias="L4ProfileName")
    __properties: ClassVar[List[str]] = ["ClientHTTPProfile", "ClientTLSProfile", "ClientTcpProfile", "IpTos", "RTPProfile", "ServerHTTPProfile", "ServerTLSProfile", "ServerTcpProfile", "UdpProfile", "VlanPrio", "links", "L4ProfileName"]

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
        """Create an instance of TransportProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_http_profile
        if self.client_http_profile:
            _dict['ClientHTTPProfile'] = self.client_http_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_tls_profile
        if self.client_tls_profile:
            _dict['ClientTLSProfile'] = self.client_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_tcp_profile
        if self.client_tcp_profile:
            _dict['ClientTcpProfile'] = self.client_tcp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rtp_profile
        if self.rtp_profile:
            _dict['RTPProfile'] = self.rtp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_http_profile
        if self.server_http_profile:
            _dict['ServerHTTPProfile'] = self.server_http_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_tls_profile
        if self.server_tls_profile:
            _dict['ServerTLSProfile'] = self.server_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_tcp_profile
        if self.server_tcp_profile:
            _dict['ServerTcpProfile'] = self.server_tcp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of udp_profile
        if self.udp_profile:
            _dict['UdpProfile'] = self.udp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "ClientHTTPProfile": HTTPProfile.from_dict(obj["ClientHTTPProfile"]) if obj.get("ClientHTTPProfile") is not None else None,
                        "ClientTLSProfile": TLSProfile.from_dict(obj["ClientTLSProfile"]) if obj.get("ClientTLSProfile") is not None else None,
                        "ClientTcpProfile": TcpProfile.from_dict(obj["ClientTcpProfile"]) if obj.get("ClientTcpProfile") is not None else None,
                        "IpTos": obj.get("IpTos"),
                        "RTPProfile": RTPProfile.from_dict(obj["RTPProfile"]) if obj.get("RTPProfile") is not None else None,
                        "ServerHTTPProfile": HTTPProfile.from_dict(obj["ServerHTTPProfile"]) if obj.get("ServerHTTPProfile") is not None else None,
                        "ServerTLSProfile": TLSProfile.from_dict(obj["ServerTLSProfile"]) if obj.get("ServerTLSProfile") is not None else None,
                        "ServerTcpProfile": TcpProfile.from_dict(obj["ServerTcpProfile"]) if obj.get("ServerTcpProfile") is not None else None,
                        "UdpProfile": UdpProfile.from_dict(obj["UdpProfile"]) if obj.get("UdpProfile") is not None else None,
                        "VlanPrio": obj.get("VlanPrio"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "L4ProfileName": obj.get("L4ProfileName")
            ,
            "links": obj.get("links")
        })
        return _obj


