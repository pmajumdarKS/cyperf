# SessionConfig

The current session's configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | [optional] 
**session_id** | **str** | The unique identifier of the session this configuration belongs to | [optional] [readonly] 
**template_id** | **str** | The unique identifier of the CyPerf configuration template from which this configuration was created | [optional] [readonly] 
**data_model_version** | **str** | The version of the data model used for this configuration | [optional] [readonly] 
**id** | **str** | The unique identifier of the CyPerf configuration | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the configuration | [optional] 

## Example

```python
from cyperf.models.session_config import SessionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SessionConfig from a JSON string
session_config_instance = SessionConfig.from_json(json)
# print the JSON string representation of the object
print(SessionConfig.to_json())

# convert the object into a dict
session_config_dict = session_config_instance.to_dict()
# create an instance of SessionConfig from a dict
session_config_from_dict = SessionConfig.from_dict(session_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


