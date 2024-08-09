# ApiV2NotificationCountsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** | The number of notifications, regardless of their type | [optional] [readonly] 
**error** | **int** | The number of error notifications | [optional] [readonly] 
**info** | **int** | The number of informational messages | [optional] [readonly] 
**warning** | **int** | The number of warnings | [optional] [readonly] 
**data** | [**NotificationCounts**](NotificationCounts.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_v2_notification_counts_get200_response import ApiV2NotificationCountsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2NotificationCountsGet200Response from a JSON string
api_v2_notification_counts_get200_response_instance = ApiV2NotificationCountsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2NotificationCountsGet200Response.to_json())

# convert the object into a dict
api_v2_notification_counts_get200_response_dict = api_v2_notification_counts_get200_response_instance.to_dict()
# create an instance of ApiV2NotificationCountsGet200Response from a dict
api_v2_notification_counts_get200_response_from_dict = ApiV2NotificationCountsGet200Response.from_dict(api_v2_notification_counts_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


