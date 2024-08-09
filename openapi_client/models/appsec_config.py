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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.config import Config
from typing import Optional, Set
from typing_extensions import Self

class AppsecConfig(BaseModel):
    """
    AppsecConfig
    """ # noqa: E501
    config: Optional[Config] = Field(default=None, alias="Config")
    session_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the session this configuration belongs to", alias="SessionID")
    template_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the CyPerf configuration template from which this configuration was created", alias="TemplateID")
    data_model_version: Optional[StrictStr] = Field(default=None, description="The version of the data model used for this configuration", alias="dataModelVersion")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the CyPerf configuration")
    name: Optional[StrictStr] = Field(default=None, description="The name of the configuration")
    __properties: ClassVar[List[str]] = ["Config", "SessionID", "TemplateID", "dataModelVersion", "id", "name"]

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
        """Create an instance of AppsecConfig from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "session_id",
            "template_id",
            "data_model_version",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['Config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppsecConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Config": Config.from_dict(obj["Config"]) if obj.get("Config") is not None else None,
            "SessionID": obj.get("SessionID"),
            "TemplateID": obj.get("TemplateID"),
            "dataModelVersion": obj.get("dataModelVersion"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


