# openapi_client.TestOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_sessions_session_id_test_calibrate_operations_start_id_get**](TestOperationsApi.md#api_v2_sessions_session_id_test_calibrate_operations_start_id_get) | **GET** /api/v2/sessions/{sessionId}/test-calibrate/operations/start/{id} | 
[**api_v2_sessions_session_id_test_calibrate_operations_start_post**](TestOperationsApi.md#api_v2_sessions_session_id_test_calibrate_operations_start_post) | **POST** /api/v2/sessions/{sessionId}/test-calibrate/operations/start | 
[**api_v2_sessions_session_id_test_calibrate_operations_stop_id_get**](TestOperationsApi.md#api_v2_sessions_session_id_test_calibrate_operations_stop_id_get) | **GET** /api/v2/sessions/{sessionId}/test-calibrate/operations/stop/{id} | 
[**api_v2_sessions_session_id_test_calibrate_operations_stop_post**](TestOperationsApi.md#api_v2_sessions_session_id_test_calibrate_operations_stop_post) | **POST** /api/v2/sessions/{sessionId}/test-calibrate/operations/stop | 
[**api_v2_sessions_session_id_test_run_operations_abort_id_get**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_abort_id_get) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/abort/{id} | 
[**api_v2_sessions_session_id_test_run_operations_abort_post**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_abort_post) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/abort | 
[**api_v2_sessions_session_id_test_run_operations_start_id_get**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_start_id_get) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/start/{id} | 
[**api_v2_sessions_session_id_test_run_operations_start_post**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_start_post) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/start | 
[**api_v2_sessions_session_id_test_run_operations_stop_id_get**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_stop_id_get) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/stop/{id} | 
[**api_v2_sessions_session_id_test_run_operations_stop_post**](TestOperationsApi.md#api_v2_sessions_session_id_test_run_operations_stop_post) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/stop | 


# **api_v2_sessions_session_id_test_calibrate_operations_start_id_get**
> AsyncContext api_v2_sessions_session_id_test_calibrate_operations_start_id_get(session_id, id)



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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_calibrate_operations_start_id_get(session_id, id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_start_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_start_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **api_v2_sessions_session_id_test_calibrate_operations_start_post**
> AsyncContext api_v2_sessions_session_id_test_calibrate_operations_start_post(session_id)



Start calibration for the test configured in the current session.

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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_calibrate_operations_start_post(session_id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **api_v2_sessions_session_id_test_calibrate_operations_stop_id_get**
> AsyncContext api_v2_sessions_session_id_test_calibrate_operations_stop_id_get(session_id, id)



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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_calibrate_operations_stop_id_get(session_id, id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_stop_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_stop_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **api_v2_sessions_session_id_test_calibrate_operations_stop_post**
> AsyncContext api_v2_sessions_session_id_test_calibrate_operations_stop_post(session_id)



Stop calibration for the test configured in the current session.

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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_calibrate_operations_stop_post(session_id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_calibrate_operations_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **api_v2_sessions_session_id_test_run_operations_abort_id_get**
> AsyncContext api_v2_sessions_session_id_test_run_operations_abort_id_get(session_id, id)



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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_abort_id_get(session_id, id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_abort_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_abort_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **api_v2_sessions_session_id_test_run_operations_abort_post**
> AsyncContext api_v2_sessions_session_id_test_run_operations_abort_post(session_id)



Abort traffic for the test configured in the current session.

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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_abort_post(session_id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_abort_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_abort_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **api_v2_sessions_session_id_test_run_operations_start_id_get**
> AsyncContext api_v2_sessions_session_id_test_run_operations_start_id_get(session_id, id)



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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_start_id_get(session_id, id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_start_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_start_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **api_v2_sessions_session_id_test_run_operations_start_post**
> AsyncContext api_v2_sessions_session_id_test_run_operations_start_post(session_id)



Start traffic for the test configured in the current session.

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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_start_post(session_id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **api_v2_sessions_session_id_test_run_operations_stop_id_get**
> AsyncContext api_v2_sessions_session_id_test_run_operations_stop_id_get(session_id, id)



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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_stop_id_get(session_id, id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_stop_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_stop_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
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

# **api_v2_sessions_session_id_test_run_operations_stop_post**
> AsyncContext api_v2_sessions_session_id_test_run_operations_stop_post(session_id)



Stop traffic for the test configured in the current session.

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
    api_instance = openapi_client.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.api_v2_sessions_session_id_test_run_operations_stop_post(session_id)
        print("The response of TestOperationsApi->api_v2_sessions_session_id_test_run_operations_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->api_v2_sessions_session_id_test_run_operations_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

