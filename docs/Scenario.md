# Scenario


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_timeout** | **int** | The action timeout value of the Scenario. | [optional] 
**active** | **bool** | Indicates whether the scenario is enabled or not. | [optional] 
**client_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The client HTTP profile used in the Scenario. | 
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**connections_max_transactions** | **int** | The maximum number of transactions for all scenario connections. | [optional] 
**description** | **str** | The description of the Scenario. | [optional] 
**destination_hostname** | **str** |  | [optional] 
**dnn_id** | **str** |  | [optional] 
**end_point_id** | **int** | The endpoint ID of the Scenario. | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | 
**external_resource_url** | **str** | The external resource URL of the Scenario. | [optional] 
**index** | **int** | The index of the scenario. | [optional] 
**inherit_http_profile** | **bool** |  | 
**ip_preference** | [**IpPreference**](IpPreference.md) | The Ip Preference. Must be one of: IPV4_ONLY, IPV6_ONLY, BOTH_IPV4_FIRST, BOTH_IPV6_FIRST or IP_PREF_MAX. | [optional] 
**is_deprecated** | **bool** | A value that indicates if the action is deprecated. | [optional] 
**iteration_count** | **int** | The iteration counter of the Scenario. | [optional] 
**max_active_limit** | **int** | The maximum active limit of the Scenario. | [optional] 
**name** | **str** |  | 
**network_mapping** | [**NetworkMapping**](NetworkMapping.md) |  | 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**protocol_id** | **str** | The protocol ID of the Scenario. | [optional] 
**qos_flow_id** | **str** |  | [optional] 
**readonly_max_trans** | **bool** | If true, ConnectionsMaxTransactions will be readonly. | [optional] 
**server_http_profile** | [**HTTPProfile**](HTTPProfile.md) | The server HTTP profile used in the Scenario. | 
**supports_client_http_profile** | **bool** | Indicates if the scenario supports Client HTTP profile. | [optional] 
**supports_http_profiles** | **bool** | Indicates if the scenario supports HTTP profiles. | 
**supports_server_http_profile** | **bool** | Indicates if the scenario supports Server HTTP profile. | [optional] 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.scenario import Scenario

# TODO update the JSON string below
json = "{}"
# create an instance of Scenario from a JSON string
scenario_instance = Scenario.from_json(json)
# print the JSON string representation of the object
print(Scenario.to_json())

# convert the object into a dict
scenario_dict = scenario_instance.to_dict()
# create an instance of Scenario from a dict
scenario_from_dict = Scenario.from_dict(scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


