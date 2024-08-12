# cyperf.ConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_config_categories_get**](ConfigurationsApi.md#api_v2_config_categories_get) | **GET** /api/v2/config-categories | 
[**api_v2_configs_config_id_delete**](ConfigurationsApi.md#api_v2_configs_config_id_delete) | **DELETE** /api/v2/configs/{configId} | 
[**api_v2_configs_config_id_get**](ConfigurationsApi.md#api_v2_configs_config_id_get) | **GET** /api/v2/configs/{configId} | 
[**api_v2_configs_config_id_patch**](ConfigurationsApi.md#api_v2_configs_config_id_patch) | **PATCH** /api/v2/configs/{configId} | 
[**api_v2_configs_config_id_put**](ConfigurationsApi.md#api_v2_configs_config_id_put) | **PUT** /api/v2/configs/{configId} | 
[**api_v2_configs_get**](ConfigurationsApi.md#api_v2_configs_get) | **GET** /api/v2/configs | 
[**api_v2_configs_operations_batch_delete_id_get**](ConfigurationsApi.md#api_v2_configs_operations_batch_delete_id_get) | **GET** /api/v2/configs/operations/batch-delete/{id} | 
[**api_v2_configs_operations_batch_delete_post**](ConfigurationsApi.md#api_v2_configs_operations_batch_delete_post) | **POST** /api/v2/configs/operations/batch-delete | 
[**api_v2_configs_operations_export_all_id_get**](ConfigurationsApi.md#api_v2_configs_operations_export_all_id_get) | **GET** /api/v2/configs/operations/exportAll/{id} | 
[**api_v2_configs_operations_export_all_post**](ConfigurationsApi.md#api_v2_configs_operations_export_all_post) | **POST** /api/v2/configs/operations/exportAll | 
[**api_v2_configs_operations_import_all_id_get**](ConfigurationsApi.md#api_v2_configs_operations_import_all_id_get) | **GET** /api/v2/configs/operations/importAll/{id} | 
[**api_v2_configs_operations_import_all_post**](ConfigurationsApi.md#api_v2_configs_operations_import_all_post) | **POST** /api/v2/configs/operations/importAll | 
[**api_v2_configs_operations_import_id_get**](ConfigurationsApi.md#api_v2_configs_operations_import_id_get) | **GET** /api/v2/configs/operations/import/{id} | 
[**api_v2_configs_operations_import_post**](ConfigurationsApi.md#api_v2_configs_operations_import_post) | **POST** /api/v2/configs/operations/import | 
[**api_v2_configs_post**](ConfigurationsApi.md#api_v2_configs_post) | **POST** /api/v2/configs | 
[**api_v2_resources_custom_import_operations_get**](ConfigurationsApi.md#api_v2_resources_custom_import_operations_get) | **GET** /api/v2/resources/custom-import-operations | 


# **api_v2_config_categories_get**
> ApiV2ConfigCategoriesGet200Response api_v2_config_categories_get(take=take, skip=skip)



Get the list of available configuration categories.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_config_categories_get200_response import ApiV2ConfigCategoriesGet200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_config_categories_get(take=take, skip=skip)
        print("The response of ConfigurationsApi->api_v2_config_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_config_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2ConfigCategoriesGet200Response**](ApiV2ConfigCategoriesGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of configuration categories |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_config_id_delete**
> api_v2_configs_config_id_delete(config_id)



Delete a particular configuration.

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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.

    try:
        api_instance.api_v2_configs_config_id_delete(config_id)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_config_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 

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
**204** | The configuration was successfully deleted. |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_config_id_get**
> ConfigMetadata api_v2_configs_config_id_get(config_id, include=include, resolve_dependencies=resolve_dependencies)



Get a particular configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included (eg. 'configData'). (optional)
    resolve_dependencies = 'resolve_dependencies_example' # str | Specifies if the content of the referenced files (action payloads and TLS files) should be included. (optional)

    try:
        api_response = api_instance.api_v2_configs_config_id_get(config_id, include=include, resolve_dependencies=resolve_dependencies)
        print("The response of ConfigurationsApi->api_v2_configs_config_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_config_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **include** | **str**| Specifies if the sub-fields that are objects should be included (eg. &#39;configData&#39;). | [optional] 
 **resolve_dependencies** | **str**| Specifies if the content of the referenced files (action payloads and TLS files) should be included. | [optional] 

### Return type

[**ConfigMetadata**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-zip, application/zip, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested configuration |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_config_id_patch**
> api_v2_configs_config_id_patch(config_id, config_metadata=config_metadata)



Update a particular configuration. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    config_metadata = cyperf.ConfigMetadata() # ConfigMetadata |  (optional)

    try:
        api_instance.api_v2_configs_config_id_patch(config_id, config_metadata=config_metadata)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_config_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **config_metadata** | [**ConfigMetadata**](ConfigMetadata.md)|  | [optional] 

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
**204** | The configuration was successfully updated. |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_config_id_put**
> ConfigMetadata api_v2_configs_config_id_put(config_id, config_metadata=config_metadata)



Update a particular configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_id = 'config_id_example' # str | The ID of the config.
    config_metadata = cyperf.ConfigMetadata() # ConfigMetadata |  (optional)

    try:
        api_response = api_instance.api_v2_configs_config_id_put(config_id, config_metadata=config_metadata)
        print("The response of ConfigurationsApi->api_v2_configs_config_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_config_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The ID of the config. | 
 **config_metadata** | [**ConfigMetadata**](ConfigMetadata.md)|  | [optional] 

### Return type

[**ConfigMetadata**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated configuration |  -  |
**400** | Bad request |  -  |
**404** | A configuration with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_get**
> ApiV2ConfigsGet200Response api_v2_configs_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)



Get all the configurations available to the current user.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_configs_get200_response import ApiV2ConfigsGet200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)

    try:
        api_response = api_instance.api_v2_configs_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)
        print("The response of ConfigurationsApi->api_v2_configs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_get: %s\n" % e)
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

### Return type

[**ApiV2ConfigsGet200Response**](ApiV2ConfigsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of configurations |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_operations_batch_delete_id_get**
> AsyncContext api_v2_configs_operations_batch_delete_id_get(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_configs_operations_batch_delete_id_get(id)
        print("The response of ConfigurationsApi->api_v2_configs_operations_batch_delete_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_batch_delete_id_get: %s\n" % e)
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

# **api_v2_configs_operations_batch_delete_post**
> AsyncContext api_v2_configs_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)



Remove multiple configurations.

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
    api_instance = cyperf.ConfigurationsApi(api_client)
    api_v2_agents_operations_batch_delete_post_request_inner = [cyperf.ApiV2AgentsOperationsBatchDeletePostRequestInner()] # List[ApiV2AgentsOperationsBatchDeletePostRequestInner] |  (optional)

    try:
        api_response = api_instance.api_v2_configs_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)
        print("The response of ConfigurationsApi->api_v2_configs_operations_batch_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_batch_delete_post: %s\n" % e)
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

# **api_v2_configs_operations_export_all_id_get**
> AsyncContext api_v2_configs_operations_export_all_id_get(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_configs_operations_export_all_id_get(id)
        print("The response of ConfigurationsApi->api_v2_configs_operations_export_all_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_export_all_id_get: %s\n" % e)
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

# **api_v2_configs_operations_export_all_post**
> AsyncContext api_v2_configs_operations_export_all_post(export_all_operation=export_all_operation)



Export all configurations owned by the current user. Optionally, provide a list of config IDs to export.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_all_operation import ExportAllOperation
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    export_all_operation = cyperf.ExportAllOperation() # ExportAllOperation |  (optional)

    try:
        api_response = api_instance.api_v2_configs_operations_export_all_post(export_all_operation=export_all_operation)
        print("The response of ConfigurationsApi->api_v2_configs_operations_export_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_export_all_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_all_operation** | [**ExportAllOperation**](ExportAllOperation.md)|  | [optional] 

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

# **api_v2_configs_operations_import_all_id_get**
> AsyncContext api_v2_configs_operations_import_all_id_get(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_configs_operations_import_all_id_get(id)
        print("The response of ConfigurationsApi->api_v2_configs_operations_import_all_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_import_all_id_get: %s\n" % e)
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

# **api_v2_configs_operations_import_all_post**
> AsyncContext api_v2_configs_operations_import_all_post(import_all_operation=import_all_operation)



Import all configurations from the specified file.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.import_all_operation import ImportAllOperation
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    import_all_operation = cyperf.ImportAllOperation() # ImportAllOperation |  (optional)

    try:
        api_response = api_instance.api_v2_configs_operations_import_all_post(import_all_operation=import_all_operation)
        print("The response of ConfigurationsApi->api_v2_configs_operations_import_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_import_all_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_all_operation** | [**ImportAllOperation**](ImportAllOperation.md)|  | [optional] 

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

# **api_v2_configs_operations_import_id_get**
> AsyncContext api_v2_configs_operations_import_id_get(id)



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
    api_instance = cyperf.ConfigurationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_configs_operations_import_id_get(id)
        print("The response of ConfigurationsApi->api_v2_configs_operations_import_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_import_id_get: %s\n" % e)
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

# **api_v2_configs_operations_import_post**
> AsyncContext api_v2_configs_operations_import_post(body=body)



Import a single configuration from the specified file.

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
    api_instance = cyperf.ConfigurationsApi(api_client)
    body = None # bytearray |  (optional)

    try:
        api_response = api_instance.api_v2_configs_operations_import_post(body=body)
        print("The response of ConfigurationsApi->api_v2_configs_operations_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_operations_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-zip, application/zip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configs_post**
> List[ConfigMetadata] api_v2_configs_post(config_metadata=config_metadata)



Save or import a new configuration. If the ConfigData field is not provided, this is implemented as a Save operation, only recording the metadata.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.config_metadata import ConfigMetadata
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    config_metadata = [cyperf.ConfigMetadata()] # List[ConfigMetadata] |  (optional)

    try:
        api_response = api_instance.api_v2_configs_post(config_metadata=config_metadata)
        print("The response of ConfigurationsApi->api_v2_configs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_configs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_metadata** | [**List[ConfigMetadata]**](ConfigMetadata.md)|  | [optional] 

### Return type

[**List[ConfigMetadata]**](ConfigMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-zip, application/zip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The configuration that was saved or imported |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_resources_custom_import_operations_get**
> ApiV2ResourcesCustomImportOperationsGet200Response api_v2_resources_custom_import_operations_get(take=take, skip=skip)



Get all the custom import config operations.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_resources_custom_import_operations_get200_response import ApiV2ResourcesCustomImportOperationsGet200Response
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
    api_instance = cyperf.ConfigurationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_resources_custom_import_operations_get(take=take, skip=skip)
        print("The response of ConfigurationsApi->api_v2_resources_custom_import_operations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->api_v2_resources_custom_import_operations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2ResourcesCustomImportOperationsGet200Response**](ApiV2ResourcesCustomImportOperationsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of custom import config operations |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

