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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from cyperf.models.api_link import APILink
from cyperf.models.attack_track import AttackTrack
from cyperf.models.connection import Connection
from cyperf.models.endpoint import Endpoint
from cyperf.models.http_profile import HTTPProfile
from cyperf.models.ip_preference import IpPreference
from cyperf.models.network_mapping import NetworkMapping
from cyperf.models.params import Params
from cyperf.models.tls_profile import TLSProfile
from cyperf.models.update_network_mapping import UpdateNetworkMapping
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class Attack(BaseModel):
    """
    Attack
    """ # noqa: E501
    action_timeout: Optional[StrictInt] = Field(default=None, description="The action timeout value of the Scenario.", alias="ActionTimeout")
    active: Optional[StrictBool] = Field(default=None, description="Indicates whether the scenario is enabled or not.", alias="Active")
    client_http_profile: Optional[HTTPProfile] = Field(default=None, description="The client HTTP profile used in the Scenario.", alias="ClientHTTPProfile")
    connections: Optional[List[Connection]] = Field(default=None, alias="Connections")
    connections_max_transactions: Optional[StrictInt] = Field(default=None, description="The maximum number of transactions for all scenario connections.", alias="ConnectionsMaxTransactions")
    description: Optional[StrictStr] = Field(default=None, description="The description of the Scenario.", alias="Description")
    destination_hostname: Optional[StrictStr] = Field(default=None, alias="DestinationHostname")
    dnn_id: Optional[StrictStr] = Field(default=None, alias="DnnId")
    end_point_id: Optional[StrictInt] = Field(default=None, description="The endpoint ID of the Scenario.", alias="EndPointID")
    endpoints: Optional[List[Endpoint]] = Field(default=None, alias="Endpoints")
    external_resource_url: Optional[StrictStr] = Field(default=None, description="The external resource URL of the Scenario.", alias="ExternalResourceURL")
    index: Optional[StrictInt] = Field(default=None, description="The index of the scenario.", alias="Index")
    inherit_http_profile: Optional[StrictBool] = Field(default=None, alias="InheritHTTPProfile")
    ip_preference: Optional[IpPreference] = Field(default=None, description="The Ip Preference. Must be one of: IPV4_ONLY, IPV6_ONLY, BOTH_IPV4_FIRST, BOTH_IPV6_FIRST or IP_PREF_MAX.", alias="IpPreference")
    is_deprecated: Optional[StrictBool] = Field(default=None, description="A value that indicates if the action is deprecated.", alias="IsDeprecated")
    iteration_count: Optional[StrictInt] = Field(default=None, description="The iteration counter of the Scenario.", alias="IterationCount")
    max_active_limit: Optional[StrictInt] = Field(default=None, description="The maximum active limit of the Scenario.", alias="MaxActiveLimit")
    name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="Name")
    network_mapping: Optional[NetworkMapping] = Field(default=None, alias="NetworkMapping")
    params: Optional[List[Params]] = Field(default=None, alias="Params")
    protocol_id: Optional[StrictStr] = Field(default=None, description="The protocol ID of the Scenario.", alias="ProtocolID")
    qos_flow_id: Optional[StrictStr] = Field(default=None, alias="QosFlowId")
    readonly_max_trans: Optional[StrictBool] = Field(default=None, description="If true, ConnectionsMaxTransactions will be readonly.", alias="ReadonlyMaxTrans")
    server_http_profile: Optional[HTTPProfile] = Field(default=None, description="The server HTTP profile used in the Scenario.", alias="ServerHTTPProfile")
    supports_client_http_profile: Optional[StrictBool] = Field(default=None, description="Indicates if the scenario supports Client HTTP profile.", alias="SupportsClientHTTPProfile")
    supports_http_profiles: Optional[StrictBool] = Field(default=None, description="Indicates if the scenario supports HTTP profiles.", alias="SupportsHTTPProfiles")
    supports_server_http_profile: Optional[StrictBool] = Field(default=None, description="Indicates if the scenario supports Server HTTP profile.", alias="SupportsServerHTTPProfile")
    id: Optional[StrictStr] = None
    links: Optional[List[APILink]] = None
    client_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ClientTLSProfile")
    inherit_tls: Optional[StrictBool] = Field(default=None, alias="InheritTLS")
    server_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ServerTLSProfile")
    supports_tls: Optional[StrictBool] = Field(default=None, alias="SupportsTLS")
    tracks: Optional[List[AttackTrack]] = Field(default=None, alias="Tracks")
    create: Optional[List[Union[StrictBytes, StrictStr]]] = None
    modify_excluded_dut_recursively: Optional[List[UpdateNetworkMapping]] = Field(default=None, alias="modify-excluded-dut-recursively")
    modify_tags_recursively: Optional[List[UpdateNetworkMapping]] = Field(default=None, alias="modify-tags-recursively")
    __properties: ClassVar[List[str]] = ["ActionTimeout", "Active", "ClientHTTPProfile", "Connections", "ConnectionsMaxTransactions", "Description", "DestinationHostname", "DnnId", "EndPointID", "Endpoints", "ExternalResourceURL", "Index", "InheritHTTPProfile", "IpPreference", "IsDeprecated", "IterationCount", "MaxActiveLimit", "Name", "NetworkMapping", "Params", "ProtocolID", "QosFlowId", "ReadonlyMaxTrans", "ServerHTTPProfile", "SupportsClientHTTPProfile", "SupportsHTTPProfiles", "SupportsServerHTTPProfile", "id", "links", "ClientTLSProfile", "InheritTLS", "ServerTLSProfile", "SupportsTLS", "Tracks", "create", "modify-excluded-dut-recursively", "modify-tags-recursively"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^[^\"\\]+$", value):
            raise ValueError(r"must validate the regular expression /^$|^[^\"\\]+$/")
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
        """Create an instance of Attack from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item in self.connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Connections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Endpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of network_mapping
        if self.network_mapping:
            _dict['NetworkMapping'] = self.network_mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item in self.params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Params'] = _items
        # override the default output from pydantic by calling `to_dict()` of server_http_profile
        if self.server_http_profile:
            _dict['ServerHTTPProfile'] = self.server_http_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of client_tls_profile
        if self.client_tls_profile:
            _dict['ClientTLSProfile'] = self.client_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_tls_profile
        if self.server_tls_profile:
            _dict['ServerTLSProfile'] = self.server_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tracks (list)
        _items = []
        if self.tracks:
            for _item in self.tracks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Tracks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modify_excluded_dut_recursively (list)
        _items = []
        if self.modify_excluded_dut_recursively:
            for _item in self.modify_excluded_dut_recursively:
                if _item:
                    _items.append(_item.to_dict())
            _dict['modify-excluded-dut-recursively'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modify_tags_recursively (list)
        _items = []
        if self.modify_tags_recursively:
            for _item in self.modify_tags_recursively:
                if _item:
                    _items.append(_item.to_dict())
            _dict['modify-tags-recursively'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Attack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "ActionTimeout": obj.get("ActionTimeout"),
                        "Active": obj.get("Active"),
                        "ClientHTTPProfile": HTTPProfile.from_dict(obj["ClientHTTPProfile"]) if obj.get("ClientHTTPProfile") is not None else None,
                        "Connections": [Connection.from_dict(_item) for _item in obj["Connections"]] if obj.get("Connections") is not None else None,
                        "ConnectionsMaxTransactions": obj.get("ConnectionsMaxTransactions"),
                        "Description": obj.get("Description"),
                        "DestinationHostname": obj.get("DestinationHostname"),
                        "DnnId": obj.get("DnnId"),
                        "EndPointID": obj.get("EndPointID"),
                        "Endpoints": [Endpoint.from_dict(_item) for _item in obj["Endpoints"]] if obj.get("Endpoints") is not None else None,
                        "ExternalResourceURL": obj.get("ExternalResourceURL"),
                        "Index": obj.get("Index"),
                        "InheritHTTPProfile": obj.get("InheritHTTPProfile"),
                        "IpPreference": obj.get("IpPreference"),
                        "IsDeprecated": obj.get("IsDeprecated"),
                        "IterationCount": obj.get("IterationCount"),
                        "MaxActiveLimit": obj.get("MaxActiveLimit"),
                        "Name": obj.get("Name"),
                        "NetworkMapping": NetworkMapping.from_dict(obj["NetworkMapping"]) if obj.get("NetworkMapping") is not None else None,
                        "Params": [Params.from_dict(_item) for _item in obj["Params"]] if obj.get("Params") is not None else None,
                        "ProtocolID": obj.get("ProtocolID"),
                        "QosFlowId": obj.get("QosFlowId"),
                        "ReadonlyMaxTrans": obj.get("ReadonlyMaxTrans"),
                        "ServerHTTPProfile": HTTPProfile.from_dict(obj["ServerHTTPProfile"]) if obj.get("ServerHTTPProfile") is not None else None,
                        "SupportsClientHTTPProfile": obj.get("SupportsClientHTTPProfile"),
                        "SupportsHTTPProfiles": obj.get("SupportsHTTPProfiles"),
                        "SupportsServerHTTPProfile": obj.get("SupportsServerHTTPProfile"),
                        "id": obj.get("id"),
                        "links": [APILink.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "ClientTLSProfile": TLSProfile.from_dict(obj["ClientTLSProfile"]) if obj.get("ClientTLSProfile") is not None else None,
                        "InheritTLS": obj.get("InheritTLS"),
                        "ServerTLSProfile": TLSProfile.from_dict(obj["ServerTLSProfile"]) if obj.get("ServerTLSProfile") is not None else None,
                        "SupportsTLS": obj.get("SupportsTLS"),
                        "Tracks": [AttackTrack.from_dict(_item) for _item in obj["Tracks"]] if obj.get("Tracks") is not None else None,
                        "create": obj.get("create"),
                        "modify-excluded-dut-recursively": [UpdateNetworkMapping.from_dict(_item) for _item in obj["modify-excluded-dut-recursively"]] if obj.get("modify-excluded-dut-recursively") is not None else None,
                        "modify-tags-recursively": [UpdateNetworkMapping.from_dict(_item) for _item in obj["modify-tags-recursively"]] if obj.get("modify-tags-recursively") is not None else None
            ,
            "links": obj.get("links")
        })
        return _obj


