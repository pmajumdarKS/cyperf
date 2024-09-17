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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from cyperf.models.feature import Feature
from cyperf.models.link import Link
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class License(BaseModel):
    """
    The license information.
    """ # noqa: E501
    activation_code: StrictStr = Field(description="The activation code that uniquely identifies the license", alias="activationCode")
    days_left_to_expire: StrictInt = Field(description="Days left to expire, value is negative if expired.", alias="daysLeftToExpire")
    expiry_date: StrictStr = Field(description="Expiry date of the license", alias="expiryDate")
    features: List[Feature] = Field(description="Features of the activation code")
    is_expired: StrictBool = Field(description="Expired flag.", alias="isExpired")
    links: List[Link] = Field(description="Hypermedia links.")
    maintenance_date: StrictStr = Field(description="Maintenance date of the license", alias="maintenanceDate")
    part_number_description: StrictStr = Field(description="Part number description", alias="partNumberDescription")
    part_number_id: StrictStr = Field(description="Part number id.", alias="partNumberId")
    product: StrictStr = Field(description="The product for which the license was generated")
    quantity: StrictInt = Field(description="Quantity installed of the license")
    __properties: ClassVar[List[str]] = ["activationCode", "daysLeftToExpire", "expiryDate", "features", "isExpired", "links", "maintenanceDate", "partNumberDescription", "partNumberId", "product", "quantity"]

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
        """Create an instance of License from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
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
        """Create an instance of License from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "activationCode": obj.get("activationCode"),
                        "daysLeftToExpire": obj.get("daysLeftToExpire"),
                        "expiryDate": obj.get("expiryDate"),
                        "features": [Feature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
                        "isExpired": obj.get("isExpired"),
                        "links": [Link.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
                        "maintenanceDate": obj.get("maintenanceDate"),
                        "partNumberDescription": obj.get("partNumberDescription"),
                        "partNumberId": obj.get("partNumberId"),
                        "product": obj.get("product"),
                        "quantity": obj.get("quantity")
            ,
            "links": obj.get("links")
        })
        return _obj


