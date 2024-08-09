# ApiV2SessionsSessionIdConfigDocsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_api_definitions** | [**Dict[str, ConfigMetadataConfigDataValue]**](ConfigMetadataConfigDataValue.md) | The OpenAPI definitions for CyPerf data model | [optional] 
**data** | [**OpenAPIDefinitions**](OpenAPIDefinitions.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_v2_sessions_session_id_config_docs_get200_response import ApiV2SessionsSessionIdConfigDocsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2SessionsSessionIdConfigDocsGet200Response from a JSON string
api_v2_sessions_session_id_config_docs_get200_response_instance = ApiV2SessionsSessionIdConfigDocsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2SessionsSessionIdConfigDocsGet200Response.to_json())

# convert the object into a dict
api_v2_sessions_session_id_config_docs_get200_response_dict = api_v2_sessions_session_id_config_docs_get200_response_instance.to_dict()
# create an instance of ApiV2SessionsSessionIdConfigDocsGet200Response from a dict
api_v2_sessions_session_id_config_docs_get200_response_from_dict = ApiV2SessionsSessionIdConfigDocsGet200Response.from_dict(api_v2_sessions_session_id_config_docs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


