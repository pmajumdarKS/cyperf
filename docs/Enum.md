# Enum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[Choice]**](Choice.md) | The constant values accepted by the enum | [optional] 
**default** | **str** | The default value of the enum | [optional] 

## Example

```python
from cyperf.models.enum import Enum

# TODO update the JSON string below
json = "{}"
# create an instance of Enum from a JSON string
enum_instance = Enum.from_json(json)
# print the JSON string representation of the object
print(Enum.to_json())

# convert the object into a dict
enum_dict = enum_instance.to_dict()
# create an instance of Enum from a dict
enum_from_dict = Enum.from_dict(enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


