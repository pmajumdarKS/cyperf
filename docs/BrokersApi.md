# cyperf.BrokersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_brokers_broker_id_delete**](BrokersApi.md#api_v2_brokers_broker_id_delete) | **DELETE** /api/v2/brokers/{brokerId} | 
[**api_v2_brokers_broker_id_get**](BrokersApi.md#api_v2_brokers_broker_id_get) | **GET** /api/v2/brokers/{brokerId} | 
[**api_v2_brokers_broker_id_patch**](BrokersApi.md#api_v2_brokers_broker_id_patch) | **PATCH** /api/v2/brokers/{brokerId} | 
[**api_v2_brokers_get**](BrokersApi.md#api_v2_brokers_get) | **GET** /api/v2/brokers | 
[**api_v2_brokers_post**](BrokersApi.md#api_v2_brokers_post) | **POST** /api/v2/brokers | 


# **api_v2_brokers_broker_id_delete**
> api_v2_brokers_broker_id_delete(broker_id)



Remove a particular broker.

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
    api_instance = cyperf.BrokersApi(api_client)
    broker_id = 'broker_id_example' # str | The ID of the broker.

    try:
        api_instance.api_v2_brokers_broker_id_delete(broker_id)
    except Exception as e:
        print("Exception when calling BrokersApi->api_v2_brokers_broker_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**| The ID of the broker. | 

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
**204** | The broker was successfully removed. |  -  |
**400** | Bad request |  -  |
**404** | A broker with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_brokers_broker_id_get**
> Broker api_v2_brokers_broker_id_get(broker_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.broker import Broker
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
    api_instance = cyperf.BrokersApi(api_client)
    broker_id = 'broker_id_example' # str | The ID of the broker.

    try:
        api_response = api_instance.api_v2_brokers_broker_id_get(broker_id)
        print("The response of BrokersApi->api_v2_brokers_broker_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokersApi->api_v2_brokers_broker_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**| The ID of the broker. | 

### Return type

[**Broker**](Broker.md)

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

# **api_v2_brokers_broker_id_patch**
> api_v2_brokers_broker_id_patch(broker_id, broker=broker)



Update a particular broker.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.broker import Broker
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
    api_instance = cyperf.BrokersApi(api_client)
    broker_id = 'broker_id_example' # str | The ID of the broker.
    broker = cyperf.Broker() # Broker |  (optional)

    try:
        api_instance.api_v2_brokers_broker_id_patch(broker_id, broker=broker)
    except Exception as e:
        print("Exception when calling BrokersApi->api_v2_brokers_broker_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_id** | **str**| The ID of the broker. | 
 **broker** | [**Broker**](Broker.md)|  | [optional] 

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
**204** | The broker was successfully updated. |  -  |
**400** | Bad request |  -  |
**404** | A broker with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_brokers_get**
> ApiV2BrokersGet200Response api_v2_brokers_get(take=take, skip=skip)



Get all the currently available brokers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_brokers_get200_response import ApiV2BrokersGet200Response
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
    api_instance = cyperf.BrokersApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.api_v2_brokers_get(take=take, skip=skip)
        print("The response of BrokersApi->api_v2_brokers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokersApi->api_v2_brokers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**ApiV2BrokersGet200Response**](ApiV2BrokersGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of external brokers that the application should connect to |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_brokers_post**
> List[Broker] api_v2_brokers_post(broker=broker)



Register an external broker.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.broker import Broker
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
    api_instance = cyperf.BrokersApi(api_client)
    broker = [cyperf.Broker()] # List[Broker] |  (optional)

    try:
        api_response = api_instance.api_v2_brokers_post(broker=broker)
        print("The response of BrokersApi->api_v2_brokers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokersApi->api_v2_brokers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker** | [**List[Broker]**](Broker.md)|  | [optional] 

### Return type

[**List[Broker]**](Broker.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The broker that was registered |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

