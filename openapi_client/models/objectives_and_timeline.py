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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.advanced_settings import AdvancedSettings
from openapi_client.models.secondary_objective import SecondaryObjective
from openapi_client.models.specific_objective import SpecificObjective
from openapi_client.models.timeline_segment import TimelineSegment
from typing import Optional, Set
from typing_extensions import Self

class ObjectivesAndTimeline(BaseModel):
    """
    ObjectivesAndTimeline
    """ # noqa: E501
    advanced_settings: Optional[AdvancedSettings] = Field(default=None, alias="AdvancedSettings")
    primary_objective: SpecificObjective = Field(alias="PrimaryObjective")
    secondary_objective: SecondaryObjective = Field(alias="SecondaryObjective")
    secondary_objectives: Optional[List[SpecificObjective]] = Field(default=None, description="Deprecated. Use SecondaryObjective instead.", alias="SecondaryObjectives")
    timeline_segments: Optional[List[TimelineSegment]] = Field(default=None, description="Deprecated. Use PrimaryObjective.Timeline instead.", alias="TimelineSegments")
    __properties: ClassVar[List[str]] = ["AdvancedSettings", "PrimaryObjective", "SecondaryObjective", "SecondaryObjectives", "TimelineSegments"]

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
        """Create an instance of ObjectivesAndTimeline from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of advanced_settings
        if self.advanced_settings:
            _dict['AdvancedSettings'] = self.advanced_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_objective
        if self.primary_objective:
            _dict['PrimaryObjective'] = self.primary_objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_objective
        if self.secondary_objective:
            _dict['SecondaryObjective'] = self.secondary_objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_objectives (list)
        _items = []
        if self.secondary_objectives:
            for _item_secondary_objectives in self.secondary_objectives:
                if _item_secondary_objectives:
                    _items.append(_item_secondary_objectives.to_dict())
            _dict['SecondaryObjectives'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in timeline_segments (list)
        _items = []
        if self.timeline_segments:
            for _item_timeline_segments in self.timeline_segments:
                if _item_timeline_segments:
                    _items.append(_item_timeline_segments.to_dict())
            _dict['TimelineSegments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectivesAndTimeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AdvancedSettings": AdvancedSettings.from_dict(obj["AdvancedSettings"]) if obj.get("AdvancedSettings") is not None else None,
            "PrimaryObjective": SpecificObjective.from_dict(obj["PrimaryObjective"]) if obj.get("PrimaryObjective") is not None else None,
            "SecondaryObjective": SecondaryObjective.from_dict(obj["SecondaryObjective"]) if obj.get("SecondaryObjective") is not None else None,
            "SecondaryObjectives": [SpecificObjective.from_dict(_item) for _item in obj["SecondaryObjectives"]] if obj.get("SecondaryObjectives") is not None else None,
            "TimelineSegments": [TimelineSegment.from_dict(_item) for _item in obj["TimelineSegments"]] if obj.get("TimelineSegments") is not None else None
        })
        return _obj


