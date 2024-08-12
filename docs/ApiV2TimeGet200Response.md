# ApiV2TimeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now** | **int** | A Unix timestamp that indicates the current cluster time | [optional] 
**data** | [**TimeValue**](TimeValue.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_time_get200_response import ApiV2TimeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2TimeGet200Response from a JSON string
api_v2_time_get200_response_instance = ApiV2TimeGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2TimeGet200Response.to_json())

# convert the object into a dict
api_v2_time_get200_response_dict = api_v2_time_get200_response_instance.to_dict()
# create an instance of ApiV2TimeGet200Response from a dict
api_v2_time_get200_response_from_dict = ApiV2TimeGet200Response.from_dict(api_v2_time_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


