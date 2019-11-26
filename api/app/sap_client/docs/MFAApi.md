# app.sap_client.MFAApi

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate_soft_token_using_post1**](MFAApi.md#deactivate_soft_token_using_post1) | **POST** /softTokens/deactivate | Deactivate soft token
[**generate_token_by_key_using_post1**](MFAApi.md#generate_token_by_key_using_post1) | **POST** /tokens/generateByKey | Generate token by key
[**generate_token_using_post1**](MFAApi.md#generate_token_using_post1) | **POST** /tokens/generate | Generates a token
[**register_soft_token_using_post1**](MFAApi.md#register_soft_token_using_post1) | **POST** /softTokens/register | Register user and return soft token
[**url_authorization_using_post1**](MFAApi.md#url_authorization_using_post1) | **POST** /tokens/urlAuthorization | urlAuthorization
[**validate_soft_token_using_post1**](MFAApi.md#validate_soft_token_using_post1) | **POST** /softTokens/validate | Validate soft token
[**validate_token_using_post1**](MFAApi.md#validate_token_using_post1) | **POST** /tokens/validate | Validates a token


# **deactivate_soft_token_using_post1**
> MfaSoftTokenValidateResponse deactivate_soft_token_using_post1(body)

Deactivate soft token

Deactivates soft token for account

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.SoftTokenRequest() # SoftTokenRequest | 

try:
    # Deactivate soft token
    api_response = api_instance.deactivate_soft_token_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->deactivate_soft_token_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoftTokenRequest**](SoftTokenRequest.md)|  | 

### Return type

[**MfaSoftTokenValidateResponse**](MfaSoftTokenValidateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **generate_token_by_key_using_post1**
> GenerateTokenResponse generate_token_by_key_using_post1(body)

Generate token by key

Generate a token associated to a specific key.

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.GenerateSoftTokenByKeyRequest() # GenerateSoftTokenByKeyRequest | 

try:
    # Generate token by key
    api_response = api_instance.generate_token_by_key_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->generate_token_by_key_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateSoftTokenByKeyRequest**](GenerateSoftTokenByKeyRequest.md)|  | 

### Return type

[**GenerateTokenResponse**](GenerateTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **generate_token_using_post1**
> GenerateTokenResponse generate_token_using_post1(body)

Generates a token

Generates a soft token to be used with a token generator app such as Google Authenticator. Token will be sent to given phone number.

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.GenerateSoftTokenRequest() # GenerateSoftTokenRequest | 

try:
    # Generates a token
    api_response = api_instance.generate_token_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->generate_token_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateSoftTokenRequest**](GenerateSoftTokenRequest.md)|  | 

### Return type

[**GenerateTokenResponse**](GenerateTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **register_soft_token_using_post1**
> MfaSoftToken register_soft_token_using_post1(body)

Register user and return soft token

Register a user and generate a soft token for that user which can be used in token generator apps

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.SoftTokenRequest() # SoftTokenRequest | 

try:
    # Register user and return soft token
    api_response = api_instance.register_soft_token_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->register_soft_token_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoftTokenRequest**](SoftTokenRequest.md)|  | 

### Return type

[**MfaSoftToken**](MfaSoftToken.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **url_authorization_using_post1**
> UrlAuthResponse url_authorization_using_post1(body)

urlAuthorization

Generate a URL authorization link that will be used as a second authentication mechanism.

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.UrlAuthorizationRequest() # UrlAuthorizationRequest | 

try:
    # urlAuthorization
    api_response = api_instance.url_authorization_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->url_authorization_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlAuthorizationRequest**](UrlAuthorizationRequest.md)|  | 

### Return type

[**UrlAuthResponse**](UrlAuthResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **validate_soft_token_using_post1**
> MfaSoftTokenValidateResponse validate_soft_token_using_post1(body)

Validate soft token

Checks the validity of a soft token for a given user.

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.ValidateSoftTokenRequest() # ValidateSoftTokenRequest | 

try:
    # Validate soft token
    api_response = api_instance.validate_soft_token_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->validate_soft_token_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateSoftTokenRequest**](ValidateSoftTokenRequest.md)|  | 

### Return type

[**MfaSoftTokenValidateResponse**](MfaSoftTokenValidateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

# **validate_token_using_post1**
> ValidateTokenResponse validate_token_using_post1(body)

Validates a token

Validates the token received as a parameter, verifying that it is still valid.

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
api_instance = app.sap_client.MFAApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.SoftTokenValidateRequest() # SoftTokenValidateRequest | 

try:
    # Validates a token
    api_response = api_instance.validate_token_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MFAApi->validate_token_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoftTokenValidateRequest**](SoftTokenValidateRequest.md)|  | 

### Return type

[**ValidateTokenResponse**](ValidateTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

