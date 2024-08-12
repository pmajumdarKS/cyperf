# ApiV2ResultsResultIdFilesGet200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResultFileMetadata]**](ResultFileMetadata.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_results_result_id_files_get200_response_one_of import ApiV2ResultsResultIdFilesGet200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ResultsResultIdFilesGet200ResponseOneOf from a JSON string
api_v2_results_result_id_files_get200_response_one_of_instance = ApiV2ResultsResultIdFilesGet200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiV2ResultsResultIdFilesGet200ResponseOneOf.to_json())

# convert the object into a dict
api_v2_results_result_id_files_get200_response_one_of_dict = api_v2_results_result_id_files_get200_response_one_of_instance.to_dict()
# create an instance of ApiV2ResultsResultIdFilesGet200ResponseOneOf from a dict
api_v2_results_result_id_files_get200_response_one_of_from_dict = ApiV2ResultsResultIdFilesGet200ResponseOneOf.from_dict(api_v2_results_result_id_files_get200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


