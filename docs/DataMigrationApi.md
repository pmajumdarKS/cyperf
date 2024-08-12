# cyperf.DataMigrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_controller_migration_operations_export_id_get**](DataMigrationApi.md#api_v2_controller_migration_operations_export_id_get) | **GET** /api/v2/controller-migration/operations/export/{id} | 
[**api_v2_controller_migration_operations_export_post**](DataMigrationApi.md#api_v2_controller_migration_operations_export_post) | **POST** /api/v2/controller-migration/operations/export | 
[**api_v2_controller_migration_operations_import_id_get**](DataMigrationApi.md#api_v2_controller_migration_operations_import_id_get) | **GET** /api/v2/controller-migration/operations/import/{id} | 
[**api_v2_controller_migration_operations_import_post**](DataMigrationApi.md#api_v2_controller_migration_operations_import_post) | **POST** /api/v2/controller-migration/operations/import | 


# **api_v2_controller_migration_operations_export_id_get**
> AsyncContext api_v2_controller_migration_operations_export_id_get(id)



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
    api_instance = cyperf.DataMigrationApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_controller_migration_operations_export_id_get(id)
        print("The response of DataMigrationApi->api_v2_controller_migration_operations_export_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->api_v2_controller_migration_operations_export_id_get: %s\n" % e)
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

# **api_v2_controller_migration_operations_export_post**
> AsyncContext api_v2_controller_migration_operations_export_post(export_package_operation=export_package_operation)



Export the data from the controller as a package.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.async_context import AsyncContext
from cyperf.models.export_package_operation import ExportPackageOperation
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
    api_instance = cyperf.DataMigrationApi(api_client)
    export_package_operation = cyperf.ExportPackageOperation() # ExportPackageOperation |  (optional)

    try:
        api_response = api_instance.api_v2_controller_migration_operations_export_post(export_package_operation=export_package_operation)
        print("The response of DataMigrationApi->api_v2_controller_migration_operations_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->api_v2_controller_migration_operations_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_package_operation** | [**ExportPackageOperation**](ExportPackageOperation.md)|  | [optional] 

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

# **api_v2_controller_migration_operations_import_id_get**
> AsyncContext api_v2_controller_migration_operations_import_id_get(id)



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
    api_instance = cyperf.DataMigrationApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_controller_migration_operations_import_id_get(id)
        print("The response of DataMigrationApi->api_v2_controller_migration_operations_import_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->api_v2_controller_migration_operations_import_id_get: %s\n" % e)
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

# **api_v2_controller_migration_operations_import_post**
> AsyncContext api_v2_controller_migration_operations_import_post(file=file)



Import the data from the supplied package into the controller.

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
    api_instance = cyperf.DataMigrationApi(api_client)
    file = None # bytearray |  (optional)

    try:
        api_response = api_instance.api_v2_controller_migration_operations_import_post(file=file)
        print("The response of DataMigrationApi->api_v2_controller_migration_operations_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataMigrationApi->api_v2_controller_migration_operations_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

