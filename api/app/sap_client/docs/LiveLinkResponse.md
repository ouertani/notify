# LiveLinkResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_error_code** | **int** | Internal error code, present only if error occurs. | [optional] 
**debug_message** | **str** | Debug message describing the problem, present only if error occurs. | [optional] 
**doc_url** | **str** | Unique locator for the doc generated in relation to the request. | [optional] 
**http_status_code** | **str** | HTTP status code returned by API Gateway. | [optional] 
**livelink_order_ids** | [**list[DestOrderId]**](DestOrderId.md) | List of all mobile numbers to which message is sent along with list of all order IDs when sent data is processed successfully. | [optional] 
**user_message** | **str** | The error message describing the problem, present only if error occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


