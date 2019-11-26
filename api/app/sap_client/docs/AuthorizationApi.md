# app.sap_client.AuthorizationApi

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_authorization_using_post1**](AuthorizationApi.md#token_authorization_using_post1) | **POST** /oauth/token | Request Authorization
[**validate_using_post1**](AuthorizationApi.md#validate_using_post1) | **POST** /oauth/token/validate | Validate Authorization


# **token_authorization_using_post1**
> AccessToken token_authorization_using_post1(grant_type, refresh_token=refresh_token)

Request Authorization

Returns an OAuth2 bearer token in exchange for the client credentials provided as parameters.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import app.sap_client
from app.sap_client.rest import ApiException
from pprint import pprint
configuration = app.sap_client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://livelink.sapmobileservices.com/api
configuration.host = "https://livelink.sapmobileservices.com/api"
# Create an instance of the API class
api_instance = app.sap_client.AuthorizationApi(app.sap_client.ApiClient(configuration))
grant_type = 'grant_type_example' # str | The grant type should be **client_credentials** to receive an access token. This access token is valid for 45 minutes. The grant type can be 'refresh_token' in subsequent API calls in order to refresh the access token before it expires.
refresh_token = 'refresh_token_example' # str | Refresh token that was received along with the access token in response to a previous request to this endpoint. The refresh token is valid for 60 minutes. It can be used in subsequent requests to this endpoint, along with **'grant_type' set as 'refresh_token'**, to get a new access token (after the previous token's 45-minute lifetime is over) without having to provide client credentials again. (optional)

try:
    # Request Authorization
    api_response = api_instance.token_authorization_using_post1(grant_type, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->token_authorization_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant type should be **client_credentials** to receive an access token. This access token is valid for 45 minutes. The grant type can be &#39;refresh_token&#39; in subsequent API calls in order to refresh the access token before it expires. | 
 **refresh_token** | **str**| Refresh token that was received along with the access token in response to a previous request to this endpoint. The refresh token is valid for 60 minutes. It can be used in subsequent requests to this endpoint, along with **&#39;grant_type&#39; set as &#39;refresh_token&#39;**, to get a new access token (after the previous token&#39;s 45-minute lifetime is over) without having to provide client credentials again. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_using_post1**
> validate_using_post1(access_token)

Validate Authorization

Determines whether the token given as parameter is still valid for authorization.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import app.sap_client
from app.sap_client.rest import ApiException
from pprint import pprint
configuration = app.sap_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://livelink.sapmobileservices.com/api
configuration.host = "https://livelink.sapmobileservices.com/api"
# Create an instance of the API class
api_instance = app.sap_client.AuthorizationApi(app.sap_client.ApiClient(configuration))
access_token = 'access_token_example' # str | The token to be validated

try:
    # Validate Authorization
    api_instance.validate_using_post1(access_token)
except ApiException as e:
    print("Exception when calling AuthorizationApi->validate_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| The token to be validated | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

