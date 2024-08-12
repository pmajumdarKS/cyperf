# cyperf.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_notification_counts_get**](NotificationsApi.md#api_v2_notification_counts_get) | **GET** /api/v2/notification-counts | 
[**api_v2_notifications_get**](NotificationsApi.md#api_v2_notifications_get) | **GET** /api/v2/notifications | 
[**api_v2_notifications_notification_id_delete**](NotificationsApi.md#api_v2_notifications_notification_id_delete) | **DELETE** /api/v2/notifications/{notificationId} | 
[**api_v2_notifications_notification_id_get**](NotificationsApi.md#api_v2_notifications_notification_id_get) | **GET** /api/v2/notifications/{notificationId} | 
[**api_v2_notifications_operations_cleanup_id_get**](NotificationsApi.md#api_v2_notifications_operations_cleanup_id_get) | **GET** /api/v2/notifications/operations/cleanup/{id} | 
[**api_v2_notifications_operations_cleanup_post**](NotificationsApi.md#api_v2_notifications_operations_cleanup_post) | **POST** /api/v2/notifications/operations/cleanup | 
[**api_v2_notifications_operations_dismiss_id_get**](NotificationsApi.md#api_v2_notifications_operations_dismiss_id_get) | **GET** /api/v2/notifications/operations/dismiss/{id} | 
[**api_v2_notifications_operations_dismiss_post**](NotificationsApi.md#api_v2_notifications_operations_dismiss_post) | **POST** /api/v2/notifications/operations/dismiss | 


# **api_v2_notification_counts_get**
> ApiV2NotificationCountsGet200Response api_v2_notification_counts_get(take=take, skip=skip, notification_id=notification_id, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, order=order, search=search)



Get the number of notifications that match the query.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_notification_counts_get200_response import ApiV2NotificationCountsGet200Response
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
    api_instance = cyperf.NotificationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    notification_id = 'notification_id_example' # str |  (optional)
    after_id = 'after_id_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    severity = 'severity_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    test_id = 'test_id_example' # str |  (optional)
    custom_tags = 'custom_tags_example' # str |  (optional)
    owner_id = 'owner_id_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    include_seen = True # bool |  (optional)
    order = 'order_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_notification_counts_get(take=take, skip=skip, notification_id=notification_id, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, order=order, search=search)
        print("The response of NotificationsApi->api_v2_notification_counts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notification_counts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **notification_id** | **str**|  | [optional] 
 **after_id** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **test_id** | **str**|  | [optional] 
 **custom_tags** | **str**|  | [optional] 
 **owner_id** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **include_seen** | **bool**|  | [optional] 
 **order** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**ApiV2NotificationCountsGet200Response**](ApiV2NotificationCountsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of notifications, aggregated by their severity |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_notifications_get**
> ApiV2NotificationsGet200Response api_v2_notifications_get(take=take, skip=skip, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, sticky=sticky, order=order, search=search)



Get all the notifications that match the query.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.api_v2_notifications_get200_response import ApiV2NotificationsGet200Response
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
    api_instance = cyperf.NotificationsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    after_id = 'after_id_example' # str |  (optional)
    var_from = 56 # int |  (optional)
    to = 56 # int |  (optional)
    severity = 'severity_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    test_id = 'test_id_example' # str |  (optional)
    custom_tags = 'custom_tags_example' # str |  (optional)
    owner_id = 'owner_id_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    include_seen = True # bool |  (optional)
    sticky = True # bool |  (optional)
    order = 'order_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_notifications_get(take=take, skip=skip, after_id=after_id, var_from=var_from, to=to, severity=severity, session_id=session_id, test_id=test_id, custom_tags=custom_tags, owner_id=owner_id, owner=owner, include_seen=include_seen, sticky=sticky, order=order, search=search)
        print("The response of NotificationsApi->api_v2_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **after_id** | **str**|  | [optional] 
 **var_from** | **int**|  | [optional] 
 **to** | **int**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **test_id** | **str**|  | [optional] 
 **custom_tags** | **str**|  | [optional] 
 **owner_id** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **include_seen** | **bool**|  | [optional] 
 **sticky** | **bool**|  | [optional] 
 **order** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**ApiV2NotificationsGet200Response**](ApiV2NotificationsGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of notifications that match the query |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_notifications_notification_id_delete**
> api_v2_notifications_notification_id_delete(notification_id)



Delete an existing notification.

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
    api_instance = cyperf.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | The ID of the notification.

    try:
        api_instance.api_v2_notifications_notification_id_delete(notification_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_notification_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The ID of the notification. | 

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
**204** | The notification was successfully deleted. |  -  |
**400** | Bad request |  -  |
**403** | The initiator of the request does not have enough privileges to perform the action. |  -  |
**404** | A notification with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_notifications_notification_id_get**
> Notification api_v2_notifications_notification_id_get(notification_id)



Get a particular notification.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import cyperf
from cyperf.models.notification import Notification
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
    api_instance = cyperf.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | The ID of the notification.

    try:
        api_response = api_instance.api_v2_notifications_notification_id_get(notification_id)
        print("The response of NotificationsApi->api_v2_notifications_notification_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_notification_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The ID of the notification. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested notification |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_notifications_operations_cleanup_id_get**
> AsyncContext api_v2_notifications_operations_cleanup_id_get(id)



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
    api_instance = cyperf.NotificationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_notifications_operations_cleanup_id_get(id)
        print("The response of NotificationsApi->api_v2_notifications_operations_cleanup_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_operations_cleanup_id_get: %s\n" % e)
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

# **api_v2_notifications_operations_cleanup_post**
> AsyncContext api_v2_notifications_operations_cleanup_post()



Cleanup all notifications that match the specified filter.

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
    api_instance = cyperf.NotificationsApi(api_client)

    try:
        api_response = api_instance.api_v2_notifications_operations_cleanup_post()
        print("The response of NotificationsApi->api_v2_notifications_operations_cleanup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_operations_cleanup_post: %s\n" % e)
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

# **api_v2_notifications_operations_dismiss_id_get**
> AsyncContext api_v2_notifications_operations_dismiss_id_get(id)



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
    api_instance = cyperf.NotificationsApi(api_client)
    id = 56 # int | The ID of the async operation.

    try:
        api_response = api_instance.api_v2_notifications_operations_dismiss_id_get(id)
        print("The response of NotificationsApi->api_v2_notifications_operations_dismiss_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_operations_dismiss_id_get: %s\n" % e)
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

# **api_v2_notifications_operations_dismiss_post**
> AsyncContext api_v2_notifications_operations_dismiss_post()



Dismiss all notifications that match the specified filter.

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
    api_instance = cyperf.NotificationsApi(api_client)

    try:
        api_response = api_instance.api_v2_notifications_operations_dismiss_post()
        print("The response of NotificationsApi->api_v2_notifications_operations_dismiss_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api_v2_notifications_operations_dismiss_post: %s\n" % e)
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

