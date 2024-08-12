# cyperf.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_agents_agent_id_delete**](AgentsApi.md#api_v2_agents_agent_id_delete) | **DELETE** /api/v2/agents/{agentId} | 
[**api_v2_agents_agent_id_get**](AgentsApi.md#api_v2_agents_agent_id_get) | **GET** /api/v2/agents/{agentId} | 
[**api_v2_agents_agent_id_patch**](AgentsApi.md#api_v2_agents_agent_id_patch) | **PATCH** /api/v2/agents/{agentId} | 
[**api_v2_agents_get**](AgentsApi.md#api_v2_agents_get) | **GET** /api/v2/agents | 
[**api_v2_agents_operations_batch_delete_id_get**](AgentsApi.md#api_v2_agents_operations_batch_delete_id_get) | **GET** /api/v2/agents/operations/batch-delete/{id} | 
[**api_v2_agents_operations_batch_delete_post**](AgentsApi.md#api_v2_agents_operations_batch_delete_post) | **POST** /api/v2/agents/operations/batch-delete | 
[**api_v2_agents_operations_export_files_id_get**](AgentsApi.md#api_v2_agents_operations_export_files_id_get) | **GET** /api/v2/agents/operations/exportFiles/{id} | 
[**api_v2_agents_operations_export_files_post**](AgentsApi.md#api_v2_agents_operations_export_files_post) | **POST** /api/v2/agents/operations/exportFiles | 
[**api_v2_agents_operations_reboot_id_get**](AgentsApi.md#api_v2_agents_operations_reboot_id_get) | **GET** /api/v2/agents/operations/reboot/{id} | 
[**api_v2_agents_operations_reboot_post**](AgentsApi.md#api_v2_agents_operations_reboot_post) | **POST** /api/v2/agents/operations/reboot | 
[**api_v2_agents_operations_release_id_get**](AgentsApi.md#api_v2_agents_operations_release_id_get) | **GET** /api/v2/agents/operations/release/{id} | 
[**api_v2_agents_operations_release_post**](AgentsApi.md#api_v2_agents_operations_release_post) | **POST** /api/v2/agents/operations/release | 
[**api_v2_agents_operations_reserve_id_get**](AgentsApi.md#api_v2_agents_operations_reserve_id_get) | **GET** /api/v2/agents/operations/reserve/{id} | 
[**api_v2_agents_operations_reserve_post**](AgentsApi.md#api_v2_agents_operations_reserve_post) | **POST** /api/v2/agents/operations/reserve | 
[**api_v2_agents_operations_set_dpdk_mode_id_get**](AgentsApi.md#api_v2_agents_operations_set_dpdk_mode_id_get) | **GET** /api/v2/agents/operations/set-dpdk-mode/{id} | 
[**api_v2_agents_operations_set_dpdk_mode_post**](AgentsApi.md#api_v2_agents_operations_set_dpdk_mode_post) | **POST** /api/v2/agents/operations/set-dpdk-mode | 
[**api_v2_agents_operations_set_ntp_id_get**](AgentsApi.md#api_v2_agents_operations_set_ntp_id_get) | **GET** /api/v2/agents/operations/set-ntp/{id} | 
[**api_v2_agents_operations_set_ntp_post**](AgentsApi.md#api_v2_agents_operations_set_ntp_post) | **POST** /api/v2/agents/operations/set-ntp | 
[**api_v2_agents_operations_update_id_get**](AgentsApi.md#api_v2_agents_operations_update_id_get) | **GET** /api/v2/agents/operations/update/{id} | 
[**api_v2_agents_operations_update_post**](AgentsApi.md#api_v2_agents_operations_update_post) | **POST** /api/v2/agents/operations/update | 
[**api_v2_tags_get**](AgentsApi.md#api_v2_tags_get) | **GET** /api/v2/tags | 


# **api_v2_agents_agent_id_delete**
> api_v2_agents_agent_id_delete(agent_id)



Remove a particular agent.

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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_instance.api_v2_agents_agent_id_delete(agent_id)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_agent_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The agent was successfully removed. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_agent_id_get**
> Agent api_v2_agents_agent_id_get(agent_id)



Get a particular agent.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.agent import Agent
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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_response = api_instance.api_v2_agents_agent_id_get(agent_id)
        print("The response of AgentsApi->api_v2_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

[**Agent**](Agent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested agent |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_agent_id_patch**
> api_v2_agents_agent_id_patch(agent_id, agent=agent)



Update a particular agent. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.agent import Agent
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
    api_instance = cyperf.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.
    agent = cyperf.Agent() # Agent |  (optional)

    try:
        api_instance.api_v2_agents_agent_id_patch(agent_id, agent=agent)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_agent_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 
 **agent** | [**Agent**](Agent.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The agent was successfully updated. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_get**
> ApiV2AgentsGet200Response api_v2_agents_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, exclude_offline=exclude_offline)



Get all the currently available agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_agents_get200_response import ApiV2AgentsGet200Response
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
    api_instance = cyperf.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
    exclude_offline = 'exclude_offline_example' # str | Indicates whether offline agents should be excluded (optional)

    try:
        api_response = api_instance.api_v2_agents_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort, exclude_offline=exclude_offline)
        print("The response of AgentsApi->api_v2_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **search_col** | **str**| A list of comma-separated columns used to search for the supplied values | [optional] 
 **search_val** | **str**| The keywords used to filter the items | [optional] 
 **filter_mode** | **str**| The operator applied to the supplied values | [optional] 
 **sort** | **str**| A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc | [optional] 
 **exclude_offline** | **str**| Indicates whether offline agents should be excluded | [optional] 

### Return type

[**ApiV2AgentsGet200Response**](ApiV2AgentsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of agents |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_batch_delete_id_get**
> AsyncContext api_v2_agents_operations_batch_delete_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_batch_delete_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_batch_delete_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_batch_delete_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_batch_delete_post**
> AsyncContext api_v2_agents_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)



Remove multiple agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_agents_operations_batch_delete_post_request_inner import ApiV2AgentsOperationsBatchDeletePostRequestInner
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    api_v2_agents_operations_batch_delete_post_request_inner = [cyperf.ApiV2AgentsOperationsBatchDeletePostRequestInner()] # List[ApiV2AgentsOperationsBatchDeletePostRequestInner] |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)
        print("The response of AgentsApi->api_v2_agents_operations_batch_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_batch_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_agents_operations_batch_delete_post_request_inner** | [**List[ApiV2AgentsOperationsBatchDeletePostRequestInner]**](ApiV2AgentsOperationsBatchDeletePostRequestInner.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_export_files_id_get**
> AsyncContext api_v2_agents_operations_export_files_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_export_files_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_export_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_export_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_export_files_post**
> AsyncContext api_v2_agents_operations_export_files_post(export_files_operation_input=export_files_operation_input)



Sends export files requests to a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_files_operation_input import ExportFilesOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    export_files_operation_input = cyperf.ExportFilesOperationInput() # ExportFilesOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_export_files_post(export_files_operation_input=export_files_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_export_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_export_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_files_operation_input** | [**ExportFilesOperationInput**](ExportFilesOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_reboot_id_get**
> AsyncContext api_v2_agents_operations_reboot_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_reboot_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_reboot_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_reboot_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_reboot_post**
> AsyncContext api_v2_agents_operations_reboot_post(reboot_operation_input=reboot_operation_input)



Reboot the agents specified in the request.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.reboot_operation_input import RebootOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    reboot_operation_input = cyperf.RebootOperationInput() # RebootOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_reboot_post(reboot_operation_input=reboot_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_reboot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_reboot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_operation_input** | [**RebootOperationInput**](RebootOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_release_id_get**
> AsyncContext api_v2_agents_operations_release_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_release_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_release_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_release_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_release_post**
> AsyncContext api_v2_agents_operations_release_post(release_operation_input=release_operation_input)



Releases all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.release_operation_input import ReleaseOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    release_operation_input = cyperf.ReleaseOperationInput() # ReleaseOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_release_post(release_operation_input=release_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_release_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_release_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_operation_input** | [**ReleaseOperationInput**](ReleaseOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_reserve_id_get**
> AsyncContext api_v2_agents_operations_reserve_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_reserve_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_reserve_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_reserve_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_reserve_post**
> AsyncContext api_v2_agents_operations_reserve_post(reserve_operation_input=reserve_operation_input)



Reserves all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.reserve_operation_input import ReserveOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    reserve_operation_input = cyperf.ReserveOperationInput() # ReserveOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_reserve_post(reserve_operation_input=reserve_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_reserve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_reserve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_operation_input** | [**ReserveOperationInput**](ReserveOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_set_dpdk_mode_id_get**
> AsyncContext api_v2_agents_operations_set_dpdk_mode_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_set_dpdk_mode_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_set_dpdk_mode_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_set_dpdk_mode_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_set_dpdk_mode_post**
> AsyncContext api_v2_agents_operations_set_dpdk_mode_post(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)



Enable/disable DPDK for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_dpdk_mode_operation_input import SetDpdkModeOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    set_dpdk_mode_operation_input = cyperf.SetDpdkModeOperationInput() # SetDpdkModeOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_set_dpdk_mode_post(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_set_dpdk_mode_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_set_dpdk_mode_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_dpdk_mode_operation_input** | [**SetDpdkModeOperationInput**](SetDpdkModeOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_set_ntp_id_get**
> AsyncContext api_v2_agents_operations_set_ntp_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_set_ntp_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_set_ntp_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_set_ntp_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_set_ntp_post**
> AsyncContext api_v2_agents_operations_set_ntp_post(set_ntp_operation_input=set_ntp_operation_input)



Set the NTP servers for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.set_ntp_operation_input import SetNtpOperationInput
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
    api_instance = cyperf.AgentsApi(api_client)
    set_ntp_operation_input = cyperf.SetNtpOperationInput() # SetNtpOperationInput |  (optional)

    try:
        api_response = api_instance.api_v2_agents_operations_set_ntp_post(set_ntp_operation_input=set_ntp_operation_input)
        print("The response of AgentsApi->api_v2_agents_operations_set_ntp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_set_ntp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ntp_operation_input** | [**SetNtpOperationInput**](SetNtpOperationInput.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_update_id_get**
> AsyncContext api_v2_agents_operations_update_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_agents_operations_update_id_get(id)
        print("The response of AgentsApi->api_v2_agents_operations_update_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_update_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the async operation. | 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the ongoing operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_agents_operations_update_post**
> AsyncContext api_v2_agents_operations_update_post()



Update agents to the recommended version.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
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
    api_instance = cyperf.AgentsApi(api_client)

    try:
        api_response = api_instance.api_v2_agents_operations_update_post()
        print("The response of AgentsApi->api_v2_agents_operations_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_agents_operations_update_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_get**
> ApiV2TagsGet200Response api_v2_tags_get(take=take, skip=skip)



Get all the currently available agent groups.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_tags_get200_response import ApiV2TagsGet200Response
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
    api_instance = cyperf.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_tags_get(take=take, skip=skip)
        print("The response of AgentsApi->api_v2_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->api_v2_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2TagsGet200Response**](ApiV2TagsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of agent groups |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

