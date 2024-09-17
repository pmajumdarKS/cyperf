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
from cyperf.models.api_link import APILink
from cyperf.models.params import Params
from cyperf.models.simulated_id_p import SimulatedIdP
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class PepDUT(BaseModel):
    """
    The Policy Enforcement Point (PEP) device under test (also known as Zero Trust device)
    """ # noqa: E501
    auth_method: Optional[Params] = Field(default=None, alias="AuthMethod")
    auth_profile_params: Optional[List[Params]] = Field(default=None, alias="AuthProfileParams")
    auth_profile_type: Optional[StrictStr] = Field(default=None, alias="AuthProfileType")
    hostname_suffix: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A suffix to be added to the Host header of all Apps/Attacks running through the DUT (default: empty string).", alias="HostnameSuffix")
    idp_type: Optional[Params] = Field(default=None, alias="IDPType")
    is_explicit_proxy: Optional[StrictBool] = Field(default=None, description="A flag indicating if PEP for the selected authentication profile is an explicit proxy", alias="IsExplicitProxy")
    pep_host: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The hostname where the traffic goes if PEP device is active.", alias="PEPHost")
    pep_port: Optional[StrictInt] = Field(default=None, description="The listen port for PEP DUT (default: 443).", alias="PEPPort")
    simulated_id_p: Optional[SimulatedIdP] = Field(default=None, alias="SimulatedIdP")
    links: Optional[List[APILink]] = None
    __properties: ClassVar[List[str]] = ["AuthMethod", "AuthProfileParams", "AuthProfileType", "HostnameSuffix", "IDPType", "IsExplicitProxy", "PEPHost", "PEPPort", "SimulatedIdP", "links"]

    @field_validator('hostname_suffix')
    def hostname_suffix_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$", value):
            raise ValueError(r"must validate the regular expression /^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/")
        return value

    @field_validator('pep_host')
    def pep_host_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$", value):
            raise ValueError(r"must validate the regular expression /^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/")
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
        """Create an instance of PepDUT from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_method
        if self.auth_method:
            _dict['AuthMethod'] = self.auth_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in auth_profile_params (list)
        _items = []
        if self.auth_profile_params:
            for _item in self.auth_profile_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AuthProfileParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of idp_type
        if self.idp_type:
            _dict['IDPType'] = self.idp_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of simulated_id_p
        if self.simulated_id_p:
            _dict['SimulatedIdP'] = self.simulated_id_p.to_dict()
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
        """Create an instance of PepDUT from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AuthMethod": Params.from_dict(obj["AuthMethod"]) if obj.get("AuthMethod") is not None else None,
                        "AuthProfileParams": [Params.from_dict(_item) for _item in obj["AuthProfileParams"]] if obj.get("AuthProfileParams") is not None else None,
                        "AuthProfileType": obj.get("AuthProfileType"),
                        "HostnameSuffix": obj.get("HostnameSuffix"),
                        "IDPType": Params.from_dict(obj["IDPType"]) if obj.get("IDPType") is not None else None,
                        "IsExplicitProxy": obj.get("IsExplicitProxy"),
                        "PEPHost": obj.get("PEPHost"),
                        "PEPPort": obj.get("PEPPort"),
                        "SimulatedIdP": SimulatedIdP.from_dict(obj["SimulatedIdP"]) if obj.get("SimulatedIdP") is not None else None,
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


