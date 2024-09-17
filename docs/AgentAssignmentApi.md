# cyperf.AgentAssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_agent_assignments_for_net_segment**](AgentAssignmentApi.md#patch_agent_assignments_for_net_segment) | **PATCH** /api/v2/sessions/{sessionId}/config/config/NetworkProfiles/{netProfileId}/IPNetworkSegment/agentAssignments | 
[**put_agent_assignments_by_id_for_net_segment**](AgentAssignmentApi.md#put_agent_assignments_by_id_for_net_segment) | **PUT** /api/v2/sessions/{sessionId}/config/config/NetworkProfiles/{netProfileId}/IPNetworkSegment/agentAssignments/ByID | 


# **patch_agent_assignments_for_net_segment**
> object patch_agent_assignments_for_net_segment(session_id, net_profile_id)



Update the agent assignments for a network group.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.AgentAssignmentApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    net_profile_id = 'net_profile_id_example' # str | The ID of the network segment. Note: this might be an INT or a STRING that holds an int value. Defaulting to string for now.

    try:
        api_response = api_instance.patch_agent_assignments_for_net_segment(session_id, net_profile_id)
        print("The response of AgentAssignmentApi->patch_agent_assignments_for_net_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAssignmentApi->patch_agent_assignments_for_net_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **net_profile_id** | **str**| The ID of the network segment. Note: this might be an INT or a STRING that holds an int value. Defaulting to string for now. | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the agent assignments for a network group. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_assignments_by_id_for_net_segment**
> object put_agent_assignments_by_id_for_net_segment(session_id, net_profile_id)



Update the list of agent IDs assigned to this network segment.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cyperf.AgentAssignmentApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    net_profile_id = 'net_profile_id_example' # str | The ID of the network segment. Note: this might be an INT or a STRING that holds an int value. Defaulting to string for now.

    try:
        api_response = api_instance.put_agent_assignments_by_id_for_net_segment(session_id, net_profile_id)
        print("The response of AgentAssignmentApi->put_agent_assignments_by_id_for_net_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentAssignmentApi->put_agent_assignments_by_id_for_net_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **net_profile_id** | **str**| The ID of the network segment. Note: this might be an INT or a STRING that holds an int value. Defaulting to string for now. | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the list of agent IDs assigned to this network segment. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

