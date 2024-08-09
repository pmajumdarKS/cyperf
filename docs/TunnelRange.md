# TunnelRange

The Tunnel Range assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisco_any_connect_settings** | [**CiscoAnyConnectSettings**](CiscoAnyConnectSettings.md) |  | 
**dcp_request_timeout** | **int** |  | 
**dns_resolver** | [**DNSResolver**](DNSResolver.md) |  | [optional] 
**f5_settings** | [**F5Settings**](F5Settings.md) |  | 
**fortinet_settings** | [**FortinetSettings**](FortinetSettings.md) |  | 
**pangp_settings** | [**PANGPSettings**](PANGPSettings.md) |  | 
**tcp_dst_port** | **int** |  | 
**tunnel_count_per_outer_ip** | **int** |  | 
**tunnel_establishment_timeout** | **int** |  | [optional] 
**vendor_type** | **str** |  | 

## Example

```python
from openapi_client.models.tunnel_range import TunnelRange

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelRange from a JSON string
tunnel_range_instance = TunnelRange.from_json(json)
# print the JSON string representation of the object
print(TunnelRange.to_json())

# convert the object into a dict
tunnel_range_dict = tunnel_range_instance.to_dict()
# create an instance of TunnelRange from a dict
tunnel_range_from_dict = TunnelRange.from_dict(tunnel_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


