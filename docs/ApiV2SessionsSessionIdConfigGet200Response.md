# ApiV2SessionsSessionIdConfigGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | [optional] 
**session_id** | **str** | The unique identifier of the session this configuration belongs to | [optional] [readonly] 
**template_id** | **str** | The unique identifier of the CyPerf configuration template from which this configuration was created | [optional] [readonly] 
**data_model_version** | **str** | The version of the data model used for this configuration | [optional] [readonly] 
**id** | **str** | The unique identifier of the CyPerf configuration | [optional] [readonly] 
**name** | **str** | The name of the configuration | [optional] 
**data** | [**AppsecConfig**](AppsecConfig.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_sessions_session_id_config_get200_response import ApiV2SessionsSessionIdConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2SessionsSessionIdConfigGet200Response from a JSON string
api_v2_sessions_session_id_config_get200_response_instance = ApiV2SessionsSessionIdConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2SessionsSessionIdConfigGet200Response.to_json())

# convert the object into a dict
api_v2_sessions_session_id_config_get200_response_dict = api_v2_sessions_session_id_config_get200_response_instance.to_dict()
# create an instance of ApiV2SessionsSessionIdConfigGet200Response from a dict
api_v2_sessions_session_id_config_get200_response_from_dict = ApiV2SessionsSessionIdConfigGet200Response.from_dict(api_v2_sessions_session_id_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


