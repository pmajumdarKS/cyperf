# ComputeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_mode** | **bool** |  | [optional] 
**app_mode** | [**AppMode**](AppMode.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ports** | [**List[Port]**](Port.md) |  | [optional] 
**slot_number** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cyperf.models.compute_node import ComputeNode

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeNode from a JSON string
compute_node_instance = ComputeNode.from_json(json)
# print the JSON string representation of the object
print(ComputeNode.to_json())

# convert the object into a dict
compute_node_dict = compute_node_instance.to_dict()
# create an instance of ComputeNode from a dict
compute_node_from_dict = ComputeNode.from_dict(compute_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


