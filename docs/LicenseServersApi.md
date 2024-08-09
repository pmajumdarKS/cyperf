# openapi_client.LicenseServersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_license_servers_get**](LicenseServersApi.md#api_v2_license_servers_get) | **GET** /api/v2/license-servers | 
[**api_v2_license_servers_license_server_id_delete**](LicenseServersApi.md#api_v2_license_servers_license_server_id_delete) | **DELETE** /api/v2/license-servers/{licenseServerId} | 
[**api_v2_license_servers_license_server_id_get**](LicenseServersApi.md#api_v2_license_servers_license_server_id_get) | **GET** /api/v2/license-servers/{licenseServerId} | 
[**api_v2_license_servers_license_server_id_patch**](LicenseServersApi.md#api_v2_license_servers_license_server_id_patch) | **PATCH** /api/v2/license-servers/{licenseServerId} | 
[**api_v2_license_servers_post**](LicenseServersApi.md#api_v2_license_servers_post) | **POST** /api/v2/license-servers | 


# **api_v2_license_servers_get**
> ApiV2LicenseServersGet200Response api_v2_license_servers_get(take=take, skip=skip)



Get all the currently available license servers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.api_v2_license_servers_get200_response import ApiV2LicenseServersGet200Response
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
    api_instance = openapi_client.LicenseServersApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_license_servers_get(take=take, skip=skip)
        print("The response of LicenseServersApi->api_v2_license_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseServersApi->api_v2_license_servers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2LicenseServersGet200Response**](ApiV2LicenseServersGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of license servers |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_license_servers_license_server_id_delete**
> api_v2_license_servers_license_server_id_delete(license_server_id)



Remove a particular license server.

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
    api_instance = openapi_client.LicenseServersApi(api_client)
    license_server_id = 'license_server_id_example' # str | The ID of the license server.

    try:
        api_instance.api_v2_license_servers_license_server_id_delete(license_server_id)
    except Exception as e:
        print("Exception when calling LicenseServersApi->api_v2_license_servers_license_server_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_server_id** | **str**| The ID of the license server. | 

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
**204** | The license server was successfully removed. |  -  |
**404** | A license server with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_license_servers_license_server_id_get**
> LicenseServerMetadata api_v2_license_servers_license_server_id_get(license_server_id)



Get a particular license server.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.license_server_metadata import LicenseServerMetadata
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
    api_instance = openapi_client.LicenseServersApi(api_client)
    license_server_id = 'license_server_id_example' # str | The ID of the license server.

    try:
        api_response = api_instance.api_v2_license_servers_license_server_id_get(license_server_id)
        print("The response of LicenseServersApi->api_v2_license_servers_license_server_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseServersApi->api_v2_license_servers_license_server_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_server_id** | **str**| The ID of the license server. | 

### Return type

[**LicenseServerMetadata**](LicenseServerMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested license server |  -  |
**404** | A license server with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_license_servers_license_server_id_patch**
> api_v2_license_servers_license_server_id_patch(license_server_id, license_server_metadata=license_server_metadata)



Update a particular license server.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.license_server_metadata import LicenseServerMetadata
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
    api_instance = openapi_client.LicenseServersApi(api_client)
    license_server_id = 'license_server_id_example' # str | The ID of the license server.
    license_server_metadata = openapi_client.LicenseServerMetadata() # LicenseServerMetadata |  (optional)

    try:
        api_instance.api_v2_license_servers_license_server_id_patch(license_server_id, license_server_metadata=license_server_metadata)
    except Exception as e:
        print("Exception when calling LicenseServersApi->api_v2_license_servers_license_server_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_server_id** | **str**| The ID of the license server. | 
 **license_server_metadata** | [**LicenseServerMetadata**](LicenseServerMetadata.md)|  | [optional] 

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
**200** | The updated license server |  -  |
**404** | A license server with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_license_servers_post**
> List[LicenseServerMetadata] api_v2_license_servers_post(license_server_metadata=license_server_metadata)



Register a license server.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.license_server_metadata import LicenseServerMetadata
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
    api_instance = openapi_client.LicenseServersApi(api_client)
    license_server_metadata = [openapi_client.LicenseServerMetadata()] # List[LicenseServerMetadata] |  (optional)

    try:
        api_response = api_instance.api_v2_license_servers_post(license_server_metadata=license_server_metadata)
        print("The response of LicenseServersApi->api_v2_license_servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseServersApi->api_v2_license_servers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_server_metadata** | [**List[LicenseServerMetadata]**](LicenseServerMetadata.md)|  | [optional] 

### Return type

[**List[LicenseServerMetadata]**](LicenseServerMetadata.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The license server that was registered |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

