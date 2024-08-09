# ApiV2DiskUsageGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | The currently available disk space (in bytes) | [optional] [readonly] 
**consumers** | [**List[Consumer]**](Consumer.md) | A list of consumers for handling logs and diagnostics storage | [optional] 
**critical_disk_space** | **bool** | A flag indicating whether disk space is critical i.e the application may become unstable | [optional] [readonly] 
**low_disk_space** | **bool** | A flag indicating whether disk space is low | [optional] [readonly] 
**message** | **str** | A user-friendly message about disk usage | [optional] [readonly] 
**pretty_available** | **str** | The currently available disk space in human-readable format | [optional] [readonly] 
**pretty_size** | **str** | The total disk size in human-readable format | [optional] [readonly] 
**size** | **int** | The total disk size (in bytes) | [optional] [readonly] 
**data** | [**DiskUsage**](DiskUsage.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_v2_disk_usage_get200_response import ApiV2DiskUsageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2DiskUsageGet200Response from a JSON string
api_v2_disk_usage_get200_response_instance = ApiV2DiskUsageGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2DiskUsageGet200Response.to_json())

# convert the object into a dict
api_v2_disk_usage_get200_response_dict = api_v2_disk_usage_get200_response_instance.to_dict()
# create an instance of ApiV2DiskUsageGet200Response from a dict
api_v2_disk_usage_get200_response_from_dict = ApiV2DiskUsageGet200Response.from_dict(api_v2_disk_usage_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


