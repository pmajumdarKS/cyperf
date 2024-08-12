# ApiV2ResourcesAuthProfilesGet200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthProfile]**](AuthProfile.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_resources_auth_profiles_get200_response_one_of import ApiV2ResourcesAuthProfilesGet200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ResourcesAuthProfilesGet200ResponseOneOf from a JSON string
api_v2_resources_auth_profiles_get200_response_one_of_instance = ApiV2ResourcesAuthProfilesGet200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiV2ResourcesAuthProfilesGet200ResponseOneOf.to_json())

# convert the object into a dict
api_v2_resources_auth_profiles_get200_response_one_of_dict = api_v2_resources_auth_profiles_get200_response_one_of_instance.to_dict()
# create an instance of ApiV2ResourcesAuthProfilesGet200ResponseOneOf from a dict
api_v2_resources_auth_profiles_get200_response_one_of_from_dict = ApiV2ResourcesAuthProfilesGet200ResponseOneOf.from_dict(api_v2_resources_auth_profiles_get200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


