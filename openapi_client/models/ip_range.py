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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.automatic_ip_type import AutomaticIpType
from openapi_client.models.ip_ver import IpVer
from openapi_client.models.vlan_range import VLANRange
from typing import Optional, Set
from typing_extensions import Self

class IPRange(BaseModel):
    """
    The IP Ranges assigned to the current test configuration
    """ # noqa: E501
    automatic_ip_type: Optional[AutomaticIpType] = Field(default=None, description="The automatic IP types, either 'ONLY_IPV4', 'ONLY_IPV6' or 'BOTH_IPV4_IPV6'.", alias="AutomaticIpType")
    count: Optional[StrictInt] = Field(default=None, description="The number of IPs generated (default: 1).", alias="Count")
    gw_auto: StrictBool = Field(description="A flag indicating if the gateway settings for the IPRange should be determined automatically (default: true).", alias="GwAuto")
    gw_start: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The gateway start IP for the IPRange (default: 10.0.0.1).", alias="GwStart")
    inner_vlan_range: Optional[VLANRange] = Field(default=None, description="The inner VLAN range assigned to the current IP range configuration", alias="InnerVlanRange")
    ip_auto: StrictBool = Field(description="A flag indicating if IP settings for the IPRange should be determined automatically (default: true).", alias="IpAuto")
    ip_incr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The IP incrementation rule (default: 0.0.0.1).", alias="IpIncr")
    ip_range_name: Annotated[str, Field(strict=True)] = Field(alias="IpRangeName")
    ip_start: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The start IP for the IPRange (default: 10.0.0.10).", alias="IpStart")
    ip_ver: IpVer = Field(description="The type of the IP. 'IPV4' and 'IPV6' are both supported currently.", alias="IpVer")
    is_emulated_router: Optional[StrictBool] = Field(default=None, alias="IsEmulatedRouter")
    mss: StrictInt = Field(description="The maximum segment size of the TCP header.", alias="Mss")
    mss_auto: StrictBool = Field(description="A flag indicating if Mss settings for the IPRange should be determined automatically (default: false).", alias="MssAuto")
    net_mask: Optional[StrictInt] = Field(default=None, description="The network mask of the IP Range (default: 16).", alias="NetMask")
    net_mask_auto: StrictBool = Field(description="A flag indicating if the network mask of the IPRange should be determined automatically (default: true).", alias="NetMaskAuto")
    id: StrictStr
    max_count_per_agent: Optional[StrictInt] = Field(default=None, description="The maximum number of IPs that should be assigned to each traffic agent for this IP range segment in a valid test (default: 1).", alias="maxCountPerAgent")
    network_tags: Optional[List[StrictStr]] = Field(default=None, description="A list of tags.", alias="networkTags")
    __properties: ClassVar[List[str]] = ["AutomaticIpType", "Count", "GwAuto", "GwStart", "InnerVlanRange", "IpAuto", "IpIncr", "IpRangeName", "IpStart", "IpVer", "IsEmulatedRouter", "Mss", "MssAuto", "NetMask", "NetMaskAuto", "id", "maxCountPerAgent", "networkTags"]

    @field_validator('gw_start')
    def gw_start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('ip_incr')
    def ip_incr_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('ip_range_name')
    def ip_range_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^$|^[^\"\\]+$", value):
            raise ValueError(r"must validate the regular expression /^$|^[^\"\\]+$/")
        return value

    @field_validator('ip_start')
    def ip_start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

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
        """Create an instance of IPRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inner_vlan_range
        if self.inner_vlan_range:
            _dict['InnerVlanRange'] = self.inner_vlan_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IPRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AutomaticIpType": obj.get("AutomaticIpType"),
            "Count": obj.get("Count"),
            "GwAuto": obj.get("GwAuto"),
            "GwStart": obj.get("GwStart"),
            "InnerVlanRange": VLANRange.from_dict(obj["InnerVlanRange"]) if obj.get("InnerVlanRange") is not None else None,
            "IpAuto": obj.get("IpAuto"),
            "IpIncr": obj.get("IpIncr"),
            "IpRangeName": obj.get("IpRangeName"),
            "IpStart": obj.get("IpStart"),
            "IpVer": obj.get("IpVer"),
            "IsEmulatedRouter": obj.get("IsEmulatedRouter"),
            "Mss": obj.get("Mss"),
            "MssAuto": obj.get("MssAuto"),
            "NetMask": obj.get("NetMask"),
            "NetMaskAuto": obj.get("NetMaskAuto"),
            "id": obj.get("id"),
            "maxCountPerAgent": obj.get("maxCountPerAgent"),
            "networkTags": obj.get("networkTags")
        })
        return _obj


