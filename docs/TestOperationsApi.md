# cyperf.TestOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_root_abort**](TestOperationsApi.md#poll_root_abort) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/abort/{id} | 
[**poll_root_start_calibration**](TestOperationsApi.md#poll_root_start_calibration) | **GET** /api/v2/sessions/{sessionId}/test-calibrate/operations/start/{id} | 
[**poll_root_start_test**](TestOperationsApi.md#poll_root_start_test) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/start/{id} | 
[**poll_root_stop_calibration**](TestOperationsApi.md#poll_root_stop_calibration) | **GET** /api/v2/sessions/{sessionId}/test-calibrate/operations/stop/{id} | 
[**poll_root_stop_test**](TestOperationsApi.md#poll_root_stop_test) | **GET** /api/v2/sessions/{sessionId}/test-run/operations/stop/{id} | 
[**start_root_abort_test**](TestOperationsApi.md#start_root_abort_test) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/abort | 
[**start_root_start_calibration**](TestOperationsApi.md#start_root_start_calibration) | **POST** /api/v2/sessions/{sessionId}/test-calibrate/operations/start | 
[**start_root_start_test**](TestOperationsApi.md#start_root_start_test) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/start | 
[**start_root_stop_calibration**](TestOperationsApi.md#start_root_stop_calibration) | **POST** /api/v2/sessions/{sessionId}/test-calibrate/operations/stop | 
[**start_root_stop_test**](TestOperationsApi.md#start_root_stop_test) | **POST** /api/v2/sessions/{sessionId}/test-run/operations/stop | 


# **poll_root_abort**
> AsyncContext poll_root_abort(session_id, id)



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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_root_abort(session_id, id)
        print("The response of TestOperationsApi->poll_root_abort:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->poll_root_abort: %s\n" % e)
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

# **poll_root_start_calibration**
> AsyncContext poll_root_start_calibration(session_id, id)



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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_root_start_calibration(session_id, id)
        print("The response of TestOperationsApi->poll_root_start_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->poll_root_start_calibration: %s\n" % e)
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

# **poll_root_start_test**
> AsyncContext poll_root_start_test(session_id, id)



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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_root_start_test(session_id, id)
        print("The response of TestOperationsApi->poll_root_start_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->poll_root_start_test: %s\n" % e)
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

# **poll_root_stop_calibration**
> AsyncContext poll_root_stop_calibration(session_id, id)



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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_root_stop_calibration(session_id, id)
        print("The response of TestOperationsApi->poll_root_stop_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->poll_root_stop_calibration: %s\n" % e)
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

# **poll_root_stop_test**
> AsyncContext poll_root_stop_test(session_id, id)



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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.poll_root_stop_test(session_id, id)
        print("The response of TestOperationsApi->poll_root_stop_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->poll_root_stop_test: %s\n" % e)
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

# **start_root_abort_test**
> AsyncContext start_root_abort_test(session_id)



Abort traffic for the test configured in the current session.

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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_root_abort_test(session_id)
        print("The response of TestOperationsApi->start_root_abort_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_root_abort_test: %s\n" % e)
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

# **start_root_start_calibration**
> AsyncContext start_root_start_calibration(session_id)



Start calibration for the test configured in the current session.

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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_root_start_calibration(session_id)
        print("The response of TestOperationsApi->start_root_start_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_root_start_calibration: %s\n" % e)
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

# **start_root_start_test**
> AsyncContext start_root_start_test(session_id)



Start traffic for the test configured in the current session.

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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_root_start_test(session_id)
        print("The response of TestOperationsApi->start_root_start_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_root_start_test: %s\n" % e)
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

# **start_root_stop_calibration**
> AsyncContext start_root_stop_calibration(session_id)



Stop calibration for the test configured in the current session.

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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_root_stop_calibration(session_id)
        print("The response of TestOperationsApi->start_root_stop_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_root_stop_calibration: %s\n" % e)
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

# **start_root_stop_test**
> AsyncContext start_root_stop_test(session_id)



Stop traffic for the test configured in the current session.

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
    api_instance = cyperf.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_root_stop_test(session_id)
        print("The response of TestOperationsApi->start_root_stop_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_root_stop_test: %s\n" % e)
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

