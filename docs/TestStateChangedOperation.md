# TestStateChangedOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | An optional message that describes the reason the test ended | [optional] 
**new_state** | **str** | An optional enum that identifies the current state of the test | [optional] 
**old_state** | **str** | An optional enum that identifies the previous state of the test | [optional] 
**owner** | **str** | An optional friendly display name for the user which initiated the operation | [optional] 
**owner_id** | **str** | An optional identifier that uniquely identifies the user which initiated the operation | [optional] 
**reason** | **str** | An optional enum that identifies the underlying reason for the test&#39;s end | [optional] 
**test_id** | **str** | The test to which the state change refers | [optional] 
**timestamp** | **int** | An optional Unix timestamp that indicates when the test state was changed | [optional] 

## Example

```python
from openapi_client.models.test_state_changed_operation import TestStateChangedOperation

# TODO update the JSON string below
json = "{}"
# create an instance of TestStateChangedOperation from a JSON string
test_state_changed_operation_instance = TestStateChangedOperation.from_json(json)
# print the JSON string representation of the object
print(TestStateChangedOperation.to_json())

# convert the object into a dict
test_state_changed_operation_dict = test_state_changed_operation_instance.to_dict()
# create an instance of TestStateChangedOperation from a dict
test_state_changed_operation_from_dict = TestStateChangedOperation.from_dict(test_state_changed_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


