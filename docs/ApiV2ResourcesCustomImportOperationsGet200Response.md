# ApiV2ResourcesCustomImportOperationsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomImportHandler]**](CustomImportHandler.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_resources_custom_import_operations_get200_response import ApiV2ResourcesCustomImportOperationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ResourcesCustomImportOperationsGet200Response from a JSON string
api_v2_resources_custom_import_operations_get200_response_instance = ApiV2ResourcesCustomImportOperationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2ResourcesCustomImportOperationsGet200Response.to_json())

# convert the object into a dict
api_v2_resources_custom_import_operations_get200_response_dict = api_v2_resources_custom_import_operations_get200_response_instance.to_dict()
# create an instance of ApiV2ResourcesCustomImportOperationsGet200Response from a dict
api_v2_resources_custom_import_operations_get200_response_from_dict = ApiV2ResourcesCustomImportOperationsGet200Response.from_dict(api_v2_resources_custom_import_operations_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


