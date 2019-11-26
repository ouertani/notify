# GenerateSoftTokenByKeyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The System account that will have access to send messages through the HUB Account. This is the MFA Account ID. | [optional] 
**key** | **str** | Generic key (any string) that can be used as a recipient address. | 
**message_body** | **str** | The message that will be carried over with the token. | [optional] 
**character_set** | **str** | The Message Character set. | [optional] 
**token_length** | **int** | Token&#39;s number of characters. | [optional] 
**pin_type** | **int** | Type of PIN. 0 for Numeric and 1 for Alphanumeric. | [optional] 
**time_out** | **int** | How long the generated token will be valid in seconds. | [optional] 
**secondarykey** | **str** | Secondary key which will be attached to the key while generating the token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


