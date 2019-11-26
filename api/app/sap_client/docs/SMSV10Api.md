# app.sap_client.SMSV10Api

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive_sms_using_post2**](SMSV10Api.md#receive_sms_using_post2) | **POST** /messages | Send SMS message


# **receive_sms_using_post2**
> SmsRequest receive_sms_using_post2(body)

Send SMS message

Send an SMS message to one or more mobile devices specified as recipients.

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
api_instance = app.sap_client.SMSV10Api(app.sap_client.ApiClient(configuration))
body = app.sap_client.SmsRequest() # SmsRequest | The SMS Request that will be sent to the API

try:
    # Send SMS message
    api_response = api_instance.receive_sms_using_post2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSV10Api->receive_sms_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsRequest**](SmsRequest.md)| The SMS Request that will be sent to the API | 

### Return type

[**SmsRequest**](SmsRequest.md)

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

