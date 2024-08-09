# PANGPSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | 
**outer_tcp_profile** | [**TcpProfile**](TcpProfile.md) |  | 
**esp_probe_retry_timeout** | **int** |  | [optional] 
**esp_probe_timeout** | **int** |  | [optional] 
**is_portal** | **bool** | A flag indicating if the tunnel is connected to PAN Portal instead of a direct connection to the PAN GP VPN Gateway (default: true). | [optional] 
**outer_tls_client_profile** | [**TLSProfile**](TLSProfile.md) |  | 
**pangp_encapsulation** | [**PANGPEncapsulation**](PANGPEncapsulation.md) |  | 
**portal_hostname** | **str** |  | 
**vpn_gateway** | **str** |  | 
**vpn_gateways** | **List[str]** |  | 

## Example

```python
from openapi_client.models.pangp_settings import PANGPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PANGPSettings from a JSON string
pangp_settings_instance = PANGPSettings.from_json(json)
# print the JSON string representation of the object
print(PANGPSettings.to_json())

# convert the object into a dict
pangp_settings_dict = pangp_settings_instance.to_dict()
# create an instance of PANGPSettings from a dict
pangp_settings_from_dict = PANGPSettings.from_dict(pangp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


