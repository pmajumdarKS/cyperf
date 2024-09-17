# AppsecSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppsecConfig**](AppsecConfig.md) |  | [optional] 

## Example

```python
from cyperf.models.appsec_session import AppsecSession

# TODO update the JSON string below
json = "{}"
# create an instance of AppsecSession from a JSON string
appsec_session_instance = AppsecSession.from_json(json)
# print the JSON string representation of the object
print(AppsecSession.to_json())

# convert the object into a dict
appsec_session_dict = appsec_session_instance.to_dict()
# create an instance of AppsecSession from a dict
appsec_session_from_dict = AppsecSession.from_dict(appsec_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


