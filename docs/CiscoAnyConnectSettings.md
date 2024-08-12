# CiscoAnyConnectSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | 
**outer_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | 
**cisco_encapsulation** | [**CiscoEncapsulation**](CiscoEncapsulation.md) |  | 
**connection_profiles** | **List[str]** |  | 
**esp_probe_retry_timeout** | **int** |  | [optional] 
**esp_probe_timeout** | **int** |  | [optional] 
**outer_tls_client_profile** | [**TLSProfile**](TLSProfile.md) |  | 
**vpn_gateway** | **str** |  | 

## Example

```python
from cyperf.models.cisco_any_connect_settings import CiscoAnyConnectSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CiscoAnyConnectSettings from a JSON string
cisco_any_connect_settings_instance = CiscoAnyConnectSettings.from_json(json)
# print the JSON string representation of the object
print(CiscoAnyConnectSettings.to_json())

# convert the object into a dict
cisco_any_connect_settings_dict = cisco_any_connect_settings_instance.to_dict()
# create an instance of CiscoAnyConnectSettings from a dict
cisco_any_connect_settings_from_dict = CiscoAnyConnectSettings.from_dict(cisco_any_connect_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


