# SmsProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID for the associated account | [optional] 
**code_tac** | **int** | Optional, region-dependent parameter. | [optional] 
**content_text_encoding** | **str** | Encoding used for the message&#39;s text | [optional] [default to 'UTF8']
**country_code** | **str** | Country code from where message was sent. | [optional] 
**cur_time** | **datetime** | Time when message was received | [optional] 
**imode_status** | **int** | Optional, region-dependent parameter. | [optional] 
**index_nber** | **int** | Optional, region-dependent paramter. | [optional] 
**keyword** | **str** | Word contained within message that was sought for in request to poll MOs. | [optional] 
**message_class** | **str** | The short message&#39;s received type. 0 &#x3D; Immediate display (flash) 1 &#x3D; Handset Specific (Live Link Default) 2 &#x3D; SIM Specific 3 &#x3D; TE Specific. | [optional] 
**mms_status** | **int** | Optional, region-dependent parameter. | [optional] 
**operator_code_mcc** | **str** | The Mobile Country Code of the operator in decimal format. | [optional] 
**operator_code_mnc** | **str** | The Mobile Network Code of the operator in decimal format. | [optional] 
**operator_id** | **str** | Unique identifier for the operator that sent the message. | [optional] 
**operator_network** | **str** | The Operator Network that sent the received message. | [optional] 
**parental_status** | **str** | Optional, region-dependent paramenter. | [optional] 
**received_service_number** | **str** | Service number sent by the mobile operator. | [optional] 
**received_time** | **str** | Time when message was received. Date portion is separated from time portion by a single space. | [optional] 
**service_id** | **int** |  | [optional] 
**session_id** | **str** | Unique identifier for the session that was lifted to receive the MO. | [optional] 
**tac_code** | **str** | The TAC code (Type Allocation Code) is used to identify the handset&#39;s terminal type. | [optional] 
**timezone** | **str** | Time zone from which the message was received. | [optional] 
**total_index** | **int** | Optional, region-dependent paramenter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


