# openapi_client.StatisticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_results_result_id_stats_get**](StatisticsApi.md#api_v2_results_result_id_stats_get) | **GET** /api/v2/results/{resultId}/stats | 
[**api_v2_results_result_id_stats_stat_id_get**](StatisticsApi.md#api_v2_results_result_id_stats_stat_id_get) | **GET** /api/v2/results/{resultId}/stats/{statId} | 
[**api_v2_stats_plugins_get**](StatisticsApi.md#api_v2_stats_plugins_get) | **GET** /api/v2/stats/plugins | 
[**api_v2_stats_plugins_operations_ingest_id_get**](StatisticsApi.md#api_v2_stats_plugins_operations_ingest_id_get) | **GET** /api/v2/stats/plugins/operations/ingest/{id} | 
[**api_v2_stats_plugins_operations_ingest_post**](StatisticsApi.md#api_v2_stats_plugins_operations_ingest_post) | **POST** /api/v2/stats/plugins/operations/ingest | 
[**api_v2_stats_plugins_plugin_id_delete**](StatisticsApi.md#api_v2_stats_plugins_plugin_id_delete) | **DELETE** /api/v2/stats/plugins/{pluginId} | 
[**api_v2_stats_plugins_post**](StatisticsApi.md#api_v2_stats_plugins_post) | **POST** /api/v2/stats/plugins | 


# **api_v2_results_result_id_stats_get**
> ApiV2ResultsResultIdStatsGet200Response api_v2_results_result_id_stats_get(result_id, take=take, skip=skip)



Get all the available queries.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_results_result_id_stats_get200_response import ApiV2ResultsResultIdStatsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_results_result_id_stats_get(result_id, take=take, skip=skip)
        print("The response of StatisticsApi->api_v2_results_result_id_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_results_result_id_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2ResultsResultIdStatsGet200Response**](ApiV2ResultsResultIdStatsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available statistics views of the current result |  -  |
**400** | Bad request |  -  |
**404** | A result with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_stats_stat_id_get**
> StatsResult api_v2_results_result_id_stats_stat_id_get(result_id, stat_id, var_from=var_from, to=to, interval=interval, use_relative_time=use_relative_time)



Query statistics

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.stats_result import StatsResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    stat_id = 'stat_id_example' # str | The ID of the stat.
    var_from = 56 # int | (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval start. Defaults to 'now-5m' (in milliseconds) for false useRelativeTime, and 0 otherwise. (optional)
    to = 56 # int | (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval end. Defaults to 'now-7s' (in milliseconds). (optional)
    interval = 56 # int | (optional) The interval used to aggregate the statistics snapshots (optional)
    use_relative_time = True # bool | (optional) Specifies if the from/to params use milliseconds from test start or UNIX time in milliseconds (optional)

    try:
        api_response = api_instance.api_v2_results_result_id_stats_stat_id_get(result_id, stat_id, var_from=var_from, to=to, interval=interval, use_relative_time=use_relative_time)
        print("The response of StatisticsApi->api_v2_results_result_id_stats_stat_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_results_result_id_stats_stat_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **stat_id** | **str**| The ID of the stat. | 
 **var_from** | **int**| (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval start. Defaults to &#39;now-5m&#39; (in milliseconds) for false useRelativeTime, and 0 otherwise. | [optional] 
 **to** | **int**| (optional) UNIX time in milliseconds or milliseconds from the test start (based on useRelativeTime flag) as the query interval end. Defaults to &#39;now-7s&#39; (in milliseconds). | [optional] 
 **interval** | **int**| (optional) The interval used to aggregate the statistics snapshots | [optional] 
 **use_relative_time** | **bool**| (optional) Specifies if the from/to params use milliseconds from test start or UNIX time in milliseconds | [optional] 

### Return type

[**StatsResult**](StatsResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully queried the statistics |  -  |
**400** | Bad request |  -  |
**404** | A result with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_stats_plugins_get**
> ApiV2StatsPluginsGet200Response api_v2_stats_plugins_get(take=take, skip=skip)



List all the plugins.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_stats_plugins_get200_response import ApiV2StatsPluginsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_stats_plugins_get(take=take, skip=skip)
        print("The response of StatisticsApi->api_v2_stats_plugins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_stats_plugins_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2StatsPluginsGet200Response**](ApiV2StatsPluginsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available plugins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_stats_plugins_operations_ingest_id_get**
> AsyncContext api_v2_stats_plugins_operations_ingest_id_get(id)



Get the state of an ongoing operation.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.async_context import AsyncContext
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_stats_plugins_operations_ingest_id_get(id)
        print("The response of StatisticsApi->api_v2_stats_plugins_operations_ingest_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_stats_plugins_operations_ingest_id_get: %s\n" % e)
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

# **api_v2_stats_plugins_operations_ingest_post**
> AsyncContext api_v2_stats_plugins_operations_ingest_post(ingest_operation=ingest_operation)



Ingest the plugin statistics.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.async_context import AsyncContext
from openapi_client.models.ingest_operation import IngestOperation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    ingest_operation = openapi_client.IngestOperation() # IngestOperation |  (optional)

    try:
        api_response = api_instance.api_v2_stats_plugins_operations_ingest_post(ingest_operation=ingest_operation)
        print("The response of StatisticsApi->api_v2_stats_plugins_operations_ingest_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_stats_plugins_operations_ingest_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_operation** | [**IngestOperation**](IngestOperation.md)|  | [optional] 

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

# **api_v2_stats_plugins_plugin_id_delete**
> api_v2_stats_plugins_plugin_id_delete(plugin_id)



Delete a particular plugin.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    plugin_id = 'plugin_id_example' # str | The ID of the plugin.

    try:
        api_instance.api_v2_stats_plugins_plugin_id_delete(plugin_id)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_stats_plugins_plugin_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| The ID of the plugin. | 

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
**204** | The plugin was successfully deleted. |  -  |
**404** | A plugin with the specified name was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_stats_plugins_post**
> List[Plugin] api_v2_stats_plugins_post(plugin=plugin)



Create new plugins.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.plugin import Plugin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatisticsApi(api_client)
    plugin = [openapi_client.Plugin()] # List[Plugin] |  (optional)

    try:
        api_response = api_instance.api_v2_stats_plugins_post(plugin=plugin)
        print("The response of StatisticsApi->api_v2_stats_plugins_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->api_v2_stats_plugins_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | [**List[Plugin]**](Plugin.md)|  | [optional] 

### Return type

[**List[Plugin]**](Plugin.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Plugins created successfully. |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

