# SmsRequestV2

This class carries all information related to a SMS request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_country_code** | **bool** | Set to true to receive Country Codes in ACKs. | [optional] [default to False]
**ack_delivered_time** | **bool** | Set to true to receive ACK delivery times. | [optional] [default to False]
**ack_final_only** | **bool** | Set to true to receive only ACKs that have Final Status. Non-final ACKs will be ignored | [optional] [default to False]
**ack_final_status** | **bool** | Set to true to receive Final Status Indicators in ACKs. | [optional] [default to False]
**ack_internal_status** | **bool** | Set to true to receive Internal Status Codes in ACKs. | [optional] [default to False]
**ack_mt_received_time** | **bool** | Set to true to receive MailSubmitTime in ACKs. | [optional] [default to False]
**ack_operator_id** | **bool** | Set to true to receive Operator IDs in ACKs. | [optional] [default to False]
**ack_time_in_gmt** | **bool** | Set to true to receive GMT time in ACKs. | [optional] [default to True]
**ack_tpoa** | **bool** | Set to &#39;true&#39; to receive TPOA in ACKs. | [optional] [default to False]
**ack_type** | **str** | Level of notification SAP will send back. | [optional] 
**acknowledgement** | **bool** | Set to true if you want to receive ACKs. | [optional] [default to False]
**callback** | **str** | Callback URL which will receive ACKs. | [optional] 
**client_id** | **int** |  | [optional] 
**content_text_encoding** | **str** | Specifies the short message&#39;s text encoding. | [optional] [default to 'UTF8']
**destination** | **list[str]** | Array of numbers that will receive the message. | 
**message** | **str** | Message body for the SMS. | 
**message_class** | **str** | Specifies the message class. Message class is an operator dependent feature.  For example: 0 &#x3D; Immediate display (flash) 1 &#x3D; Handset Specific (Live Link Default) 2 &#x3D; SIM Specific 3 &#x3D; TE Specific. | [optional] [default to '1']
**mobile_notification** | **str** |  | [optional] 
**operator_id** | **int** | Used to specify the destination operators for the message. | [optional] 
**origin** | **str** | Live Link number from which message will be sent. | [optional] 
**p_id** | **str** | When a special value is needed, it is possible to define this value inside the request by giving the hexadecimal code of the PID desired. | [optional] 
**random_id** | **int** |  | [optional] 
**session_id** | **str** | This is needed for session tracking, US campaign tracking, or other purposes. When supported by an operator, you may receive information in the SESSION_ID field of an incoming MO request. Upon receiving such information, you are expected to post it back into the SESSION_ID field of the MT reply. | [optional] 
**subject** | **str** | This field can be useful to set your own unique ID which will be returned in notifications and will ease tracking of messages statuses. | [optional] 
**validity_period** | **str** | Tells how long SAP tries to send the message.The time can be specified in weeks, days, hours or minutes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


