# PollStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_status_indicator** | **str** | Code that indicates the final delivery status of the sent message. | [optional] 
**internal_status_id** | **str** | Unique identifier for the status the message went through in intermediate steps before final delivery. | [optional] 
**message_body** | **str** | Body of the message that was sent as the SMS&#39;s content. | [optional] 
**operator_id** | **int** | Unique identifier for the operator that sent the message. | [optional] 
**order_id** | **str** | Unique identifier for the order generated in response to the send-SMS request. | [optional] 
**recipient** | **str** | Phone number that received the message. | [optional] 
**status** | **str** | Describes the state that the message went through while it was being sent. | [optional] 
**timestamp** | **datetime** | Marks the point in time that the message went through the status described in this object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


