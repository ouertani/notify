# app.sap_client.EmailApi

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email_using_post1**](EmailApi.md#send_email_using_post1) | **POST** /email/send | Send email message


# **send_email_using_post1**
> EmailChannelResponse send_email_using_post1(body)

Send email message

Send an email message to one or more email addresses specified as recipients.

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
api_instance = app.sap_client.EmailApi(app.sap_client.ApiClient(configuration))
body = app.sap_client.EmailRequest() # EmailRequest | 

try:
    # Send email message
    api_response = api_instance.send_email_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->send_email_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailRequest**](EmailRequest.md)|  | 

### Return type

[**EmailChannelResponse**](EmailChannelResponse.md)

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

