# TunnelStack

The tunnel stack assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inner_ip_range** | [**InnerIPRange**](InnerIPRange.md) |  | 
**outer_ip_range** | [**IPRange**](IPRange.md) |  | 
**tunnel_range** | [**TunnelRange**](TunnelRange.md) |  | 
**tunnel_stack_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.tunnel_stack import TunnelStack

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelStack from a JSON string
tunnel_stack_instance = TunnelStack.from_json(json)
# print the JSON string representation of the object
print(TunnelStack.to_json())

# convert the object into a dict
tunnel_stack_dict = tunnel_stack_instance.to_dict()
# create an instance of TunnelStack from a dict
tunnel_stack_from_dict = TunnelStack.from_dict(tunnel_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


