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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.application import Application
from openapi_client.models.external_resource_info import ExternalResourceInfo
from openapi_client.models.network_mapping import NetworkMapping
from openapi_client.models.objectives_and_timeline import ObjectivesAndTimeline
from openapi_client.models.traffic_settings import TrafficSettings
from openapi_client.models.update_network_mapping import UpdateNetworkMapping
from typing import Optional, Set
from typing_extensions import Self

class ApplicationProfile(BaseModel):
    """
    ApplicationProfile
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="Indicates whether the profile is enabled or not.", alias="Active")
    traffic_settings: TrafficSettings = Field(alias="TrafficSettings")
    id: StrictStr
    applications: List[Application] = Field(alias="Applications")
    default_network_mapping: NetworkMapping = Field(alias="DefaultNetworkMapping")
    name: StrictStr = Field(alias="Name")
    objectives_and_timeline: ObjectivesAndTimeline = Field(alias="ObjectivesAndTimeline")
    add_applications: Optional[List[ExternalResourceInfo]] = Field(default=None, alias="add-applications")
    modify_excluded_dut_recursively: Optional[List[UpdateNetworkMapping]] = Field(default=None, alias="modify-excluded-dut-recursively")
    modify_tags_recursively: Optional[List[UpdateNetworkMapping]] = Field(default=None, alias="modify-tags-recursively")
    reset_tags_to_default: Optional[List[Union[StrictBytes, StrictStr]]] = Field(default=None, alias="reset-tags-to-default")
    __properties: ClassVar[List[str]] = ["Active", "TrafficSettings", "id", "Applications", "DefaultNetworkMapping", "Name", "ObjectivesAndTimeline", "add-applications", "modify-excluded-dut-recursively", "modify-tags-recursively", "reset-tags-to-default"]

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
        """Create an instance of ApplicationProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of traffic_settings
        if self.traffic_settings:
            _dict['TrafficSettings'] = self.traffic_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in applications (list)
        _items = []
        if self.applications:
            for _item_applications in self.applications:
                if _item_applications:
                    _items.append(_item_applications.to_dict())
            _dict['Applications'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_network_mapping
        if self.default_network_mapping:
            _dict['DefaultNetworkMapping'] = self.default_network_mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of objectives_and_timeline
        if self.objectives_and_timeline:
            _dict['ObjectivesAndTimeline'] = self.objectives_and_timeline.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in add_applications (list)
        _items = []
        if self.add_applications:
            for _item_add_applications in self.add_applications:
                if _item_add_applications:
                    _items.append(_item_add_applications.to_dict())
            _dict['add-applications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modify_excluded_dut_recursively (list)
        _items = []
        if self.modify_excluded_dut_recursively:
            for _item_modify_excluded_dut_recursively in self.modify_excluded_dut_recursively:
                if _item_modify_excluded_dut_recursively:
                    _items.append(_item_modify_excluded_dut_recursively.to_dict())
            _dict['modify-excluded-dut-recursively'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modify_tags_recursively (list)
        _items = []
        if self.modify_tags_recursively:
            for _item_modify_tags_recursively in self.modify_tags_recursively:
                if _item_modify_tags_recursively:
                    _items.append(_item_modify_tags_recursively.to_dict())
            _dict['modify-tags-recursively'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Active": obj.get("Active"),
            "TrafficSettings": TrafficSettings.from_dict(obj["TrafficSettings"]) if obj.get("TrafficSettings") is not None else None,
            "id": obj.get("id"),
            "Applications": [Application.from_dict(_item) for _item in obj["Applications"]] if obj.get("Applications") is not None else None,
            "DefaultNetworkMapping": NetworkMapping.from_dict(obj["DefaultNetworkMapping"]) if obj.get("DefaultNetworkMapping") is not None else None,
            "Name": obj.get("Name"),
            "ObjectivesAndTimeline": ObjectivesAndTimeline.from_dict(obj["ObjectivesAndTimeline"]) if obj.get("ObjectivesAndTimeline") is not None else None,
            "add-applications": [ExternalResourceInfo.from_dict(_item) for _item in obj["add-applications"]] if obj.get("add-applications") is not None else None,
            "modify-excluded-dut-recursively": [UpdateNetworkMapping.from_dict(_item) for _item in obj["modify-excluded-dut-recursively"]] if obj.get("modify-excluded-dut-recursively") is not None else None,
            "modify-tags-recursively": [UpdateNetworkMapping.from_dict(_item) for _item in obj["modify-tags-recursively"]] if obj.get("modify-tags-recursively") is not None else None,
            "reset-tags-to-default": obj.get("reset-tags-to-default")
        })
        return _obj


