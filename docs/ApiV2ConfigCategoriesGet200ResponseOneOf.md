# ApiV2ConfigCategoriesGet200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigCategory]**](ConfigCategory.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from cyperf.models.api_v2_config_categories_get200_response_one_of import ApiV2ConfigCategoriesGet200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ConfigCategoriesGet200ResponseOneOf from a JSON string
api_v2_config_categories_get200_response_one_of_instance = ApiV2ConfigCategoriesGet200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiV2ConfigCategoriesGet200ResponseOneOf.to_json())

# convert the object into a dict
api_v2_config_categories_get200_response_one_of_dict = api_v2_config_categories_get200_response_one_of_instance.to_dict()
# create an instance of ApiV2ConfigCategoriesGet200ResponseOneOf from a dict
api_v2_config_categories_get200_response_one_of_from_dict = ApiV2ConfigCategoriesGet200ResponseOneOf.from_dict(api_v2_config_categories_get200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


