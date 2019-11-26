# SmsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** | Represents the client account. | [optional] 
**body** | **str** | The Message body for the SMS. | 
**channel** | **str** | Channel through which message will be delivered. This value should be: \&quot;SMS\&quot;. | [optional] [default to 'SMS']
**origin** | **str** | Live Link number from which message will be sent. | [optional] 
**destination** | **list[str]** | An array of destination numbers that will receive the message. | 
**ack_type** | **str** | Level of notification SAP will send back. | [optional] [default to 'ORDER']
**validity_period** | **str** | Time frame within which SAP will try to send the message. The time can be specified in weeks, days, hours or minutes. | [optional] 
**session_id** | **str** | It is needed for US campaign tracking. | [optional] 
**content_text_encoding** | **str** | Specifies the message&#39;s text encoding. | [optional] 
**subject** | **str** | Sets the message&#39;s subject. The subject will be returned in notifications and will ease tracking of message statuses. | [optional] 
**mobile_notification** | **str** | A Mobile Notification is an operator-dependent feature. | [optional] 
**operator_id** | **str** | Used to specify the destination operators for the message. | [optional] 
**message_class** | **str** | Used to specify the message class. Message class is an operator-dependent feature.  For example: 0 &#x3D; Immediate display (flash) 1 &#x3D; Handset Specific (LiveLink Default) 2 &#x3D; SIM Specific 3 &#x3D; TE Specific. | [optional] 
**p_id** | **str** |  When a special value is needed, give the hexadecimal PID code you wish the request to carry. | [optional] 
**ack_flags** | **str** | Represents various types of acknowledgements. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


