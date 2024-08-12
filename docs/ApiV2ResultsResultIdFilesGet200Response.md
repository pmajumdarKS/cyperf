# ApiV2ResultsResultIdFilesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResultFileMetadata]**](ResultFileMetadata.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_results_result_id_files_get200_response import ApiV2ResultsResultIdFilesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ResultsResultIdFilesGet200Response from a JSON string
api_v2_results_result_id_files_get200_response_instance = ApiV2ResultsResultIdFilesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2ResultsResultIdFilesGet200Response.to_json())

# convert the object into a dict
api_v2_results_result_id_files_get200_response_dict = api_v2_results_result_id_files_get200_response_instance.to_dict()
# create an instance of ApiV2ResultsResultIdFilesGet200Response from a dict
api_v2_results_result_id_files_get200_response_from_dict = ApiV2ResultsResultIdFilesGet200Response.from_dict(api_v2_results_result_id_files_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


