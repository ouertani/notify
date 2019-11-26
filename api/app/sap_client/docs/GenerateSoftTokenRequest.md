# GenerateSoftTokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The System account that will have access to send messages through the HUB Account. This is the MFA Account ID. | [optional] 
**telephone_number** | **int** | The user phone number that will receive the token. | [optional] 
**message_body** | **str** | The message that will be carried over with the token. | [optional] 
**character_set** | **str** | It is the Message Character set. | [optional] 
**token_length** | **int** | Length of characters from Minimum 4 to a Maximum of 9. | [optional] 
**pin_type** | **int** | Type of PIN. 0 for Numeric and 1 for Alphanumeric. | [optional] 
**time_out** | **int** | How long the generated token will be valid in seconds. Minimum of 30 to a Maximum of 900. For Example: 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


