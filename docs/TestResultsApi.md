# openapi_client.TestResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_results_get**](TestResultsApi.md#api_v2_results_get) | **GET** /api/v2/results | 
[**api_v2_results_operations_batch_delete_id_get**](TestResultsApi.md#api_v2_results_operations_batch_delete_id_get) | **GET** /api/v2/results/operations/batch-delete/{id} | 
[**api_v2_results_operations_batch_delete_post**](TestResultsApi.md#api_v2_results_operations_batch_delete_post) | **POST** /api/v2/results/operations/batch-delete | 
[**api_v2_results_result_id_delete**](TestResultsApi.md#api_v2_results_result_id_delete) | **DELETE** /api/v2/results/{resultId} | 
[**api_v2_results_result_id_download_all_download_all_id_get**](TestResultsApi.md#api_v2_results_result_id_download_all_download_all_id_get) | **GET** /api/v2/results/{resultId}/download-all/{downloadAllId} | 
[**api_v2_results_result_id_download_result_config_get**](TestResultsApi.md#api_v2_results_result_id_download_result_config_get) | **GET** /api/v2/results/{resultId}/download-result-config | 
[**api_v2_results_result_id_files_file_id_content_get**](TestResultsApi.md#api_v2_results_result_id_files_file_id_content_get) | **GET** /api/v2/results/{resultId}/files/{fileId}/content | 
[**api_v2_results_result_id_files_file_id_delete**](TestResultsApi.md#api_v2_results_result_id_files_file_id_delete) | **DELETE** /api/v2/results/{resultId}/files/{fileId} | 
[**api_v2_results_result_id_files_file_id_get**](TestResultsApi.md#api_v2_results_result_id_files_file_id_get) | **GET** /api/v2/results/{resultId}/files/{fileId} | 
[**api_v2_results_result_id_files_get**](TestResultsApi.md#api_v2_results_result_id_files_get) | **GET** /api/v2/results/{resultId}/files | 
[**api_v2_results_result_id_get**](TestResultsApi.md#api_v2_results_result_id_get) | **GET** /api/v2/results/{resultId} | 
[**api_v2_results_result_id_operations_generate_all_id_get**](TestResultsApi.md#api_v2_results_result_id_operations_generate_all_id_get) | **GET** /api/v2/results/{resultId}/operations/generate-all/{id} | 
[**api_v2_results_result_id_operations_generate_all_post**](TestResultsApi.md#api_v2_results_result_id_operations_generate_all_post) | **POST** /api/v2/results/{resultId}/operations/generate-all | 
[**api_v2_results_result_id_operations_generate_results_id_get**](TestResultsApi.md#api_v2_results_result_id_operations_generate_results_id_get) | **GET** /api/v2/results/{resultId}/operations/generate-results/{id} | 
[**api_v2_results_result_id_operations_generate_results_post**](TestResultsApi.md#api_v2_results_result_id_operations_generate_results_post) | **POST** /api/v2/results/{resultId}/operations/generate-results | 
[**api_v2_results_result_id_operations_load_id_get**](TestResultsApi.md#api_v2_results_result_id_operations_load_id_get) | **GET** /api/v2/results/{resultId}/operations/load/{id} | 
[**api_v2_results_result_id_operations_load_post**](TestResultsApi.md#api_v2_results_result_id_operations_load_post) | **POST** /api/v2/results/{resultId}/operations/load | 
[**api_v2_results_tags_get**](TestResultsApi.md#api_v2_results_tags_get) | **GET** /api/v2/results/tags | 


# **api_v2_results_get**
> ApiV2ResultsGet200Response api_v2_results_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)



Get all the available results.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_results_get200_response import ApiV2ResultsGet200Response
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
    api_instance = openapi_client.TestResultsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    search_col = 'search_col_example' # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'search_val_example' # str | The keywords used to filter the items (optional)
    filter_mode = 'filter_mode_example' # str | The operator applied to the supplied values (optional)
    sort = 'sort_example' # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)

    try:
        api_response = api_instance.api_v2_results_get(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)
        print("The response of TestResultsApi->api_v2_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_get: %s\n" % e)
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

[**ApiV2ResultsGet200Response**](ApiV2ResultsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of results |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_operations_batch_delete_id_get**
> AsyncContext api_v2_results_operations_batch_delete_id_get(id)



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
    api_instance = openapi_client.TestResultsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_results_operations_batch_delete_id_get(id)
        print("The response of TestResultsApi->api_v2_results_operations_batch_delete_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_operations_batch_delete_id_get: %s\n" % e)
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

# **api_v2_results_operations_batch_delete_post**
> AsyncContext api_v2_results_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)



Remove multiple results.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_agents_operations_batch_delete_post_request_inner import ApiV2AgentsOperationsBatchDeletePostRequestInner
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
    api_instance = openapi_client.TestResultsApi(api_client)
    api_v2_agents_operations_batch_delete_post_request_inner = [openapi_client.ApiV2AgentsOperationsBatchDeletePostRequestInner()] # List[ApiV2AgentsOperationsBatchDeletePostRequestInner] |  (optional)

    try:
        api_response = api_instance.api_v2_results_operations_batch_delete_post(api_v2_agents_operations_batch_delete_post_request_inner=api_v2_agents_operations_batch_delete_post_request_inner)
        print("The response of TestResultsApi->api_v2_results_operations_batch_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_operations_batch_delete_post: %s\n" % e)
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

# **api_v2_results_result_id_delete**
> api_v2_results_result_id_delete(result_id)



Delete a particular result.

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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.

    try:
        api_instance.api_v2_results_result_id_delete(result_id)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 

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
**204** | The result was successfully deleted. |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A result with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_download_all_download_all_id_get**
> api_v2_results_result_id_download_all_download_all_id_get(result_id, download_all_id)



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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    download_all_id = 'download_all_id_example' # str | The ID of the download all.

    try:
        api_instance.api_v2_results_result_id_download_all_download_all_id_get(result_id, download_all_id)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_download_all_download_all_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **download_all_id** | **str**| The ID of the download all. | 

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
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_download_result_config_get**
> ApiV2AppsecUiMetadataGet200Response api_v2_results_result_id_download_result_config_get(result_id, take=take, skip=skip)



Download the configuration associated with the result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_appsec_ui_metadata_get200_response import ApiV2AppsecUiMetadataGet200Response
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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_results_result_id_download_result_config_get(result_id, take=take, skip=skip)
        print("The response of TestResultsApi->api_v2_results_result_id_download_result_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_download_result_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2AppsecUiMetadataGet200Response**](ApiV2AppsecUiMetadataGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content of the zip file |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_file_id_content_get**
> bytearray api_v2_results_result_id_files_file_id_content_get(result_id, file_id)



Get the content of a result file.

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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    file_id = 'file_id_example' # str | The ID of the file.

    try:
        api_response = api_instance.api_v2_results_result_id_files_file_id_content_get(result_id, file_id)
        print("The response of TestResultsApi->api_v2_results_result_id_files_file_id_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_files_file_id_content_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **file_id** | **str**| The ID of the file. | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content of the result file |  -  |
**404** | A result or file with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_file_id_delete**
> api_v2_results_result_id_files_file_id_delete(result_id, file_id)



Delete a particular result file.

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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    file_id = 'file_id_example' # str | The ID of the file.

    try:
        api_instance.api_v2_results_result_id_files_file_id_delete(result_id, file_id)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_files_file_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **file_id** | **str**| The ID of the file. | 

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
**204** | The file was successfully deleted. |  -  |
**404** | A result or file with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_file_id_get**
> ResultFileMetadata api_v2_results_result_id_files_file_id_get(result_id, file_id)



Get a particular result file.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.result_file_metadata import ResultFileMetadata
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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    file_id = 'file_id_example' # str | The ID of the file.

    try:
        api_response = api_instance.api_v2_results_result_id_files_file_id_get(result_id, file_id)
        print("The response of TestResultsApi->api_v2_results_result_id_files_file_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_files_file_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **file_id** | **str**| The ID of the file. | 

### Return type

[**ResultFileMetadata**](ResultFileMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested file |  -  |
**404** | A result or file with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_files_get**
> ApiV2ResultsResultIdFilesGet200Response api_v2_results_result_id_files_get(result_id, take=take, skip=skip)



Get the list of files for a specific result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_results_result_id_files_get200_response import ApiV2ResultsResultIdFilesGet200Response
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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_results_result_id_files_get(result_id, take=take, skip=skip)
        print("The response of TestResultsApi->api_v2_results_result_id_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2ResultsResultIdFilesGet200Response**](ApiV2ResultsResultIdFilesGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of files |  -  |
**404** | A result with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_get**
> ResultMetadata api_v2_results_result_id_get(result_id)



Get a particular result.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.result_metadata import ResultMetadata
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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.

    try:
        api_response = api_instance.api_v2_results_result_id_get(result_id)
        print("The response of TestResultsApi->api_v2_results_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 

### Return type

[**ResultMetadata**](ResultMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested result |  -  |
**404** | A result with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_results_result_id_operations_generate_all_id_get**
> AsyncContext api_v2_results_result_id_operations_generate_all_id_get(result_id, id)



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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_results_result_id_operations_generate_all_id_get(result_id, id)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_generate_all_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_generate_all_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
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

# **api_v2_results_result_id_operations_generate_all_post**
> AsyncContext api_v2_results_result_id_operations_generate_all_post(result_id, generate_all_operation=generate_all_operation)



Generate all result types.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.async_context import AsyncContext
from openapi_client.models.generate_all_operation import GenerateAllOperation
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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    generate_all_operation = openapi_client.GenerateAllOperation() # GenerateAllOperation |  (optional)

    try:
        api_response = api_instance.api_v2_results_result_id_operations_generate_all_post(result_id, generate_all_operation=generate_all_operation)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_generate_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_generate_all_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
 **generate_all_operation** | [**GenerateAllOperation**](GenerateAllOperation.md)|  | [optional] 

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

# **api_v2_results_result_id_operations_generate_results_id_get**
> AsyncContext api_v2_results_result_id_operations_generate_results_id_get(result_id, id)



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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_results_result_id_operations_generate_results_id_get(result_id, id)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_generate_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_generate_results_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
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

# **api_v2_results_result_id_operations_generate_results_post**
> AsyncContext api_v2_results_result_id_operations_generate_results_post(result_id)



Export all result files zipped.

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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.

    try:
        api_response = api_instance.api_v2_results_result_id_operations_generate_results_post(result_id)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_generate_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_generate_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 

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

# **api_v2_results_result_id_operations_load_id_get**
> AsyncContext api_v2_results_result_id_operations_load_id_get(result_id, id)



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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_results_result_id_operations_load_id_get(result_id, id)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_load_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_load_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 
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

# **api_v2_results_result_id_operations_load_post**
> AsyncContext api_v2_results_result_id_operations_load_post(result_id)



Loads a completed result into a new session.

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
    api_instance = openapi_client.TestResultsApi(api_client)
    result_id = 'result_id_example' # str | The ID of the result.

    try:
        api_response = api_instance.api_v2_results_result_id_operations_load_post(result_id)
        print("The response of TestResultsApi->api_v2_results_result_id_operations_load_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_result_id_operations_load_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The ID of the result. | 

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

# **api_v2_results_tags_get**
> ApiV2ResultsTagsGet200Response api_v2_results_tags_get(take=take, skip=skip)



Get all the currently available agent groups.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_results_tags_get200_response import ApiV2ResultsTagsGet200Response
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
    api_instance = openapi_client.TestResultsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_results_tags_get(take=take, skip=skip)
        print("The response of TestResultsApi->api_v2_results_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_results_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2ResultsTagsGet200Response**](ApiV2ResultsTagsGet200Response.md)

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

