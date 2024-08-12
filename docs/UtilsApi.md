# cyperf.UtilsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_disk_usage_consumers_consumer_id_get**](UtilsApi.md#api_v2_disk_usage_consumers_consumer_id_get) | **GET** /api/v2/disk-usage/consumers/{consumerId} | 
[**api_v2_disk_usage_consumers_get**](UtilsApi.md#api_v2_disk_usage_consumers_get) | **GET** /api/v2/disk-usage/consumers | 
[**api_v2_disk_usage_get**](UtilsApi.md#api_v2_disk_usage_get) | **GET** /api/v2/disk-usage | 
[**api_v2_disk_usage_operations_cleanup_diagnostics_id_get**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_diagnostics_id_get) | **GET** /api/v2/disk-usage/operations/cleanup-diagnostics/{id} | 
[**api_v2_disk_usage_operations_cleanup_diagnostics_post**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_diagnostics_post) | **POST** /api/v2/disk-usage/operations/cleanup-diagnostics | 
[**api_v2_disk_usage_operations_cleanup_logs_id_get**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_logs_id_get) | **GET** /api/v2/disk-usage/operations/cleanup-logs/{id} | 
[**api_v2_disk_usage_operations_cleanup_logs_post**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_logs_post) | **POST** /api/v2/disk-usage/operations/cleanup-logs | 
[**api_v2_disk_usage_operations_cleanup_migration_id_get**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_migration_id_get) | **GET** /api/v2/disk-usage/operations/cleanup-migration/{id} | 
[**api_v2_disk_usage_operations_cleanup_migration_post**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_migration_post) | **POST** /api/v2/disk-usage/operations/cleanup-migration | 
[**api_v2_disk_usage_operations_cleanup_notifications_id_get**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_notifications_id_get) | **GET** /api/v2/disk-usage/operations/cleanup-notifications/{id} | 
[**api_v2_disk_usage_operations_cleanup_notifications_post**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_notifications_post) | **POST** /api/v2/disk-usage/operations/cleanup-notifications | 
[**api_v2_disk_usage_operations_cleanup_results_id_get**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_results_id_get) | **GET** /api/v2/disk-usage/operations/cleanup-results/{id} | 
[**api_v2_disk_usage_operations_cleanup_results_post**](UtilsApi.md#api_v2_disk_usage_operations_cleanup_results_post) | **POST** /api/v2/disk-usage/operations/cleanup-results | 
[**api_v2_docs_get**](UtilsApi.md#api_v2_docs_get) | **GET** /api/v2/docs | 
[**api_v2_docs_json_get**](UtilsApi.md#api_v2_docs_json_get) | **GET** /api/v2/docs.json | 
[**api_v2_docs_yaml_get**](UtilsApi.md#api_v2_docs_yaml_get) | **GET** /api/v2/docs.yaml | 
[**api_v2_log_config_get**](UtilsApi.md#api_v2_log_config_get) | **GET** /api/v2/log-config | 
[**api_v2_log_config_put**](UtilsApi.md#api_v2_log_config_put) | **PUT** /api/v2/log-config | 
[**api_v2_time_get**](UtilsApi.md#api_v2_time_get) | **GET** /api/v2/time | 


# **api_v2_disk_usage_consumers_consumer_id_get**
> Consumer api_v2_disk_usage_consumers_consumer_id_get(consumer_id)



Get the size for logs and diagnostics.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.consumer import Consumer
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
    api_instance = cyperf.UtilsApi(api_client)
    consumer_id = 'consumer_id_example' # str | The ID of the consumer.

    try:
        api_response = api_instance.api_v2_disk_usage_consumers_consumer_id_get(consumer_id)
        print("The response of UtilsApi->api_v2_disk_usage_consumers_consumer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_consumers_consumer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| The ID of the consumer. | 

### Return type

[**Consumer**](Consumer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about logs and diagnostics size |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_disk_usage_consumers_get**
> ApiV2DiskUsageConsumersGet200Response api_v2_disk_usage_consumers_get(take=take, skip=skip)



Get the list of consumers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_disk_usage_consumers_get200_response import ApiV2DiskUsageConsumersGet200Response
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
    api_instance = cyperf.UtilsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_disk_usage_consumers_get(take=take, skip=skip)
        print("The response of UtilsApi->api_v2_disk_usage_consumers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_consumers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2DiskUsageConsumersGet200Response**](ApiV2DiskUsageConsumersGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of consumers which can be either logs or diagnostics |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_disk_usage_get**
> ApiV2DiskUsageGet200Response api_v2_disk_usage_get(take=take, skip=skip)



Get information about the controller's disk usage.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_disk_usage_get200_response import ApiV2DiskUsageGet200Response
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
    api_instance = cyperf.UtilsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_disk_usage_get(take=take, skip=skip)
        print("The response of UtilsApi->api_v2_disk_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2DiskUsageGet200Response**](ApiV2DiskUsageGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The controller disk usage |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_disk_usage_operations_cleanup_diagnostics_id_get**
> AsyncContext api_v2_disk_usage_operations_cleanup_diagnostics_id_get(id)



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
    api_instance = cyperf.UtilsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_diagnostics_id_get(id)
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_diagnostics_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_diagnostics_id_get: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_diagnostics_post**
> AsyncContext api_v2_disk_usage_operations_cleanup_diagnostics_post()



Clean the system diagnostics.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_diagnostics_post()
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_diagnostics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_diagnostics_post: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_logs_id_get**
> AsyncContext api_v2_disk_usage_operations_cleanup_logs_id_get(id)



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
    api_instance = cyperf.UtilsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_logs_id_get(id)
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_logs_id_get: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_logs_post**
> AsyncContext api_v2_disk_usage_operations_cleanup_logs_post()



Clean the system logs.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_logs_post()
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_logs_post: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_migration_id_get**
> AsyncContext api_v2_disk_usage_operations_cleanup_migration_id_get(id)



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
    api_instance = cyperf.UtilsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_migration_id_get(id)
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_migration_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_migration_id_get: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_migration_post**
> AsyncContext api_v2_disk_usage_operations_cleanup_migration_post()



Clean the migration packages.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_migration_post()
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_migration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_migration_post: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_notifications_id_get**
> AsyncContext api_v2_disk_usage_operations_cleanup_notifications_id_get(id)



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
    api_instance = cyperf.UtilsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_notifications_id_get(id)
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_notifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_notifications_id_get: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_notifications_post**
> AsyncContext api_v2_disk_usage_operations_cleanup_notifications_post()



Clean all notifications.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_notifications_post()
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_notifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_notifications_post: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_results_id_get**
> AsyncContext api_v2_disk_usage_operations_cleanup_results_id_get(id)



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
    api_instance = cyperf.UtilsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_results_id_get(id)
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_results_id_get: %s\n" % e)
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

# **api_v2_disk_usage_operations_cleanup_results_post**
> AsyncContext api_v2_disk_usage_operations_cleanup_results_post()



Clean all statistics.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_disk_usage_operations_cleanup_results_post()
        print("The response of UtilsApi->api_v2_disk_usage_operations_cleanup_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_disk_usage_operations_cleanup_results_post: %s\n" % e)
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

# **api_v2_docs_get**
> api_v2_docs_get()



Get the OpenAPI definitions.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_instance.api_v2_docs_get()
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_docs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | The OpenAPI definitions |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_docs_json_get**
> api_v2_docs_json_get()



Get the OpenAPI definitions.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_instance.api_v2_docs_json_get()
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_docs_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | The OpenAPI definitions |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_docs_yaml_get**
> str api_v2_docs_yaml_get()



Get the OpenAPI definitions.

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
    api_instance = cyperf.UtilsApi(api_client)

    try:
        api_response = api_instance.api_v2_docs_yaml_get()
        print("The response of UtilsApi->api_v2_docs_yaml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_docs_yaml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/yaml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpenAPI definitions |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_log_config_get**
> ApiV2LogConfigGet200Response api_v2_log_config_get(take=take, skip=skip)



Get the current global log level.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_log_config_get200_response import ApiV2LogConfigGet200Response
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
    api_instance = cyperf.UtilsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_log_config_get(take=take, skip=skip)
        print("The response of UtilsApi->api_v2_log_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_log_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2LogConfigGet200Response**](ApiV2LogConfigGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current global log level |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_log_config_put**
> LogConfig api_v2_log_config_put(log_config=log_config)



Update the global log level for all services.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.log_config import LogConfig
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
    api_instance = cyperf.UtilsApi(api_client)
    log_config = cyperf.LogConfig() # LogConfig |  (optional)

    try:
        api_response = api_instance.api_v2_log_config_put(log_config=log_config)
        print("The response of UtilsApi->api_v2_log_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_log_config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_config** | [**LogConfig**](LogConfig.md)|  | [optional] 

### Return type

[**LogConfig**](LogConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current global log level |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_time_get**
> ApiV2TimeGet200Response api_v2_time_get(take=take, skip=skip)



Get the cluster time.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_time_get200_response import ApiV2TimeGet200Response
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
    api_instance = cyperf.UtilsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_time_get(take=take, skip=skip)
        print("The response of UtilsApi->api_v2_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->api_v2_time_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2TimeGet200Response**](ApiV2TimeGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current cluster time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

