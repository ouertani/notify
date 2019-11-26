# app.sap_client.SMSV20Api

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_mo_using_get1**](SMSV20Api.md#query_mo_using_get1) | **GET** /v2/sms/mo | Poll MO (Mobile Originated) Responses
[**query_status_using_get1**](SMSV20Api.md#query_status_using_get1) | **GET** /v2/sms/status | Poll SMS delivery statuses
[**send_sms_using_post**](SMSV20Api.md#send_sms_using_post) | **POST** /v2/sms | Send SMS message


# **query_mo_using_get1**
> PollMoResponse query_mo_using_get1(start_utc_time, end_utc_time, page_index, keyword=keyword)

Poll MO (Mobile Originated) Responses

Pull historical data on MO (Mobile Originated) incoming replies that were received within a specific time frame.

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
api_instance = app.sap_client.SMSV20Api(app.sap_client.ApiClient(configuration))
start_utc_time = 56 # int | UTC time in 'yyyyMMddHHmm' format Example: 201709011230
end_utc_time = 56 # int | UTC time in 'yyyyMMddHHmm' format Example: 201709020130
page_index = 1 # int | Response to MO query is paginated. Each page has a size of 10, meaning it holds the details of 10 MOs. The pageIndex is the page number from which MOs are to be fetched. It can be an integer between 1 and n, where n is the number of pages available.  For example: Suppose the MO query returns 45 MOs. There will be 5 pages available. pageIndex in this case can be from 1 to 5. (default to 1)
keyword = 'keyword_example' # str | Keyword is the word to match in the MO message's body. The check is case-insensitive. For example, if keyword is 'STOP', all MOs that contain STOP in their content body will be fetched. (optional)

try:
    # Poll MO (Mobile Originated) Responses
    api_response = api_instance.query_mo_using_get1(start_utc_time, end_utc_time, page_index, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSV20Api->query_mo_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_utc_time** | **int**| UTC time in &#39;yyyyMMddHHmm&#39; format Example: 201709011230 | 
 **end_utc_time** | **int**| UTC time in &#39;yyyyMMddHHmm&#39; format Example: 201709020130 | 
 **page_index** | **int**| Response to MO query is paginated. Each page has a size of 10, meaning it holds the details of 10 MOs. The pageIndex is the page number from which MOs are to be fetched. It can be an integer between 1 and n, where n is the number of pages available.  For example: Suppose the MO query returns 45 MOs. There will be 5 pages available. pageIndex in this case can be from 1 to 5. | [default to 1]
 **keyword** | **str**| Keyword is the word to match in the MO message&#39;s body. The check is case-insensitive. For example, if keyword is &#39;STOP&#39;, all MOs that contain STOP in their content body will be fetched. | [optional] 

### Return type

[**PollMoResponse**](PollMoResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_status_using_get1**
> PollStatusResponse query_status_using_get1(start_utc_time, end_utc_time, page_index, status=status)

Poll SMS delivery statuses

Pull historical data on MT (Mobile Terminated) message delivery statuses from messages that were sent within a specific time frame.

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
api_instance = app.sap_client.SMSV20Api(app.sap_client.ApiClient(configuration))
start_utc_time = 56 # int | UTC time in 'yyyyMMddHHmm' format Example: 201709011230
end_utc_time = 56 # int | UTC time in 'yyyyMMddHHmm' format Example: 201709020130
page_index = 1 # int | Response to status query is paginated. Each page has a size of 10, meaning it holds the details of 10 ACKs. The pageIndex is the page number from which ACKs are to be fetched. It can be an integer between 1 and n, where n is the number of pages available.  For example: Suppose the status query returns 68 ACKs. There will be 7 pages available. pageIndex in this case can be from 1 to 7 (default to 1)
status = 'all' # str | Status of the messages to be fetched.  Value meanings: 'all' - All Acks are fetched 'nok' - all errors are fetched 'SENT' - all ACKs with status as 'SENT' are fetched 'DELIVERED' -  all ACKs with status as 'DELIVERED' are fetched 'RECEIVED' - all ACKs with status as 'RECEIVED' are fetched (optional) (default to 'all')

try:
    # Poll SMS delivery statuses
    api_response = api_instance.query_status_using_get1(start_utc_time, end_utc_time, page_index, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSV20Api->query_status_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_utc_time** | **int**| UTC time in &#39;yyyyMMddHHmm&#39; format Example: 201709011230 | 
 **end_utc_time** | **int**| UTC time in &#39;yyyyMMddHHmm&#39; format Example: 201709020130 | 
 **page_index** | **int**| Response to status query is paginated. Each page has a size of 10, meaning it holds the details of 10 ACKs. The pageIndex is the page number from which ACKs are to be fetched. It can be an integer between 1 and n, where n is the number of pages available.  For example: Suppose the status query returns 68 ACKs. There will be 7 pages available. pageIndex in this case can be from 1 to 7 | [default to 1]
 **status** | **str**| Status of the messages to be fetched.  Value meanings: &#39;all&#39; - All Acks are fetched &#39;nok&#39; - all errors are fetched &#39;SENT&#39; - all ACKs with status as &#39;SENT&#39; are fetched &#39;DELIVERED&#39; -  all ACKs with status as &#39;DELIVERED&#39; are fetched &#39;RECEIVED&#39; - all ACKs with status as &#39;RECEIVED&#39; are fetched | [optional] [default to &#39;all&#39;]

### Return type

[**PollStatusResponse**](PollStatusResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_using_post**
> LiveLinkResponse send_sms_using_post(body)

Send SMS message

Send an MT (Mobile Terminated) SMS message to one or more handset devices specified as recipients.

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
api_instance = app.sap_client.SMSV20Api(app.sap_client.ApiClient(configuration))
body = app.sap_client.SmsRequestV2() # SmsRequestV2 | This is a JSON object with parameters used for SMS sending. Please find a detailed explaination for the fields in the <b>Model</b> section

try:
    # Send SMS message
    api_response = api_instance.send_sms_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSV20Api->send_sms_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsRequestV2**](SmsRequestV2.md)| This is a JSON object with parameters used for SMS sending. Please find a detailed explaination for the fields in the &lt;b&gt;Model&lt;/b&gt; section | 

### Return type

[**LiveLinkResponse**](LiveLinkResponse.md)

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

