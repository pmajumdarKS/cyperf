# Certificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | **bool** |  | [optional] 
**dns_names** | **List[str]** |  | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 
**issuer** | **str** |  | [optional] [readonly] 
**not_after** | **str** |  | [optional] [readonly] 
**not_before** | **str** |  | [optional] [readonly] 
**valid_for** | **int** |  | [optional] 

## Example

```python
from cyperf.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print(Certificate.to_json())

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_from_dict = Certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


