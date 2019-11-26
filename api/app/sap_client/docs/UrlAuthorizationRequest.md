# UrlAuthorizationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The System account that will have access to send messages through the HUB Account. This is the MFA account ID. | [optional] 
**telephone_number** | **int** | The user phone number that will receive the token. | 
**email_address** | **int** | Email address that will receive the token. | 
**message_body** | **str** | The message that will be carried over with the token. | [optional] 
**character_set** | **str** | It is the Message Character set. | [optional] 
**token_length** | **int** | Number of characters the token will contain. | [optional] 
**pin_type** | **int** | Type of PIN. 0 for Numeric and 1 for Alphanumeric. | [optional] 
**time_out** | **int** | Token&#39;s validity lifetime in seconds. | [optional] 
**secondarykey** | **str** | Secondary key which will be attached to the key while generating the token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


