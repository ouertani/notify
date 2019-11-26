# app.sap-client
The SAP Live Link 365 is a communication platform as a service (CPaaS) that leverages robust delivery technology, SAP’s global relationships, and the power of SAP’s Cloud Platform to provide affordable, scalable, and global messaging solutions for best in class SMS management.

The `app.sap_client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.15
* six >= 1.10
* certifi
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with app.sap-client,
you can run the following:

```python
from __future__ import print_function
import time
import app.sap_client
from app.sap_client.rest import ApiException
from pprint import pprint

configuration = app.sap_client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://livelink.sapmobileservices.com/api
configuration.host = "https://livelink.sapmobileservices.com/api"
# Create an instance of the API class
api_instance = app.sap_client.AuthorizationApi(app.sap_client.ApiClient(configuration))
grant_type = 'grant_type_example' # str | The grant type should be **client_credentials** to receive an access token. This access token is valid for 45 minutes. The grant type can be 'refresh_token' in subsequent API calls in order to refresh the access token before it expires.
refresh_token = 'refresh_token_example' # str | Refresh token that was received along with the access token in response to a previous request to this endpoint. The refresh token is valid for 60 minutes. It can be used in subsequent requests to this endpoint, along with **'grant_type' set as 'refresh_token'**, to get a new access token (after the previous token's 45-minute lifetime is over) without having to provide client credentials again. (optional)

try:
    # Request Authorization
    api_response = api_instance.token_authorization_using_post1(grant_type, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationApi->token_authorization_using_post1: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorizationApi* | [**token_authorization_using_post1**](app/sap_client/docs/AuthorizationApi.md#token_authorization_using_post1) | **POST** /oauth/token | Request Authorization
*AuthorizationApi* | [**validate_using_post1**](app/sap_client/docs/AuthorizationApi.md#validate_using_post1) | **POST** /oauth/token/validate | Validate Authorization
*EmailApi* | [**send_email_using_post1**](app/sap_client/docs/EmailApi.md#send_email_using_post1) | **POST** /email/send | Send email message
*MFAApi* | [**deactivate_soft_token_using_post1**](app/sap_client/docs/MFAApi.md#deactivate_soft_token_using_post1) | **POST** /softTokens/deactivate | Deactivate soft token
*MFAApi* | [**generate_token_by_key_using_post1**](app/sap_client/docs/MFAApi.md#generate_token_by_key_using_post1) | **POST** /tokens/generateByKey | Generate token by key
*MFAApi* | [**generate_token_using_post1**](app/sap_client/docs/MFAApi.md#generate_token_using_post1) | **POST** /tokens/generate | Generates a token
*MFAApi* | [**register_soft_token_using_post1**](app/sap_client/docs/MFAApi.md#register_soft_token_using_post1) | **POST** /softTokens/register | Register user and return soft token
*MFAApi* | [**url_authorization_using_post1**](app/sap_client/docs/MFAApi.md#url_authorization_using_post1) | **POST** /tokens/urlAuthorization | urlAuthorization
*MFAApi* | [**validate_soft_token_using_post1**](app/sap_client/docs/MFAApi.md#validate_soft_token_using_post1) | **POST** /softTokens/validate | Validate soft token
*MFAApi* | [**validate_token_using_post1**](app/sap_client/docs/MFAApi.md#validate_token_using_post1) | **POST** /tokens/validate | Validates a token
*SMSV10Api* | [**receive_sms_using_post2**](app/sap_client/docs/SMSV10Api.md#receive_sms_using_post2) | **POST** /messages | Send SMS message
*SMSV20Api* | [**query_mo_using_get1**](app/sap_client/docs/SMSV20Api.md#query_mo_using_get1) | **GET** /v2/sms/mo | Poll MO (Mobile Originated) Responses
*SMSV20Api* | [**query_status_using_get1**](app/sap_client/docs/SMSV20Api.md#query_status_using_get1) | **GET** /v2/sms/status | Poll SMS delivery statuses
*SMSV20Api* | [**send_sms_using_post**](app/sap_client/docs/SMSV20Api.md#send_sms_using_post) | **POST** /v2/sms | Send SMS message


## Documentation For Models

 - [AccessToken](app/sap_client/docs/AccessToken.md)
 - [DestOrderId](app/sap_client/docs/DestOrderId.md)
 - [EmailChannelResponse](app/sap_client/docs/EmailChannelResponse.md)
 - [EmailRequest](app/sap_client/docs/EmailRequest.md)
 - [GenerateSoftTokenByKeyRequest](app/sap_client/docs/GenerateSoftTokenByKeyRequest.md)
 - [GenerateSoftTokenRequest](app/sap_client/docs/GenerateSoftTokenRequest.md)
 - [GenerateTokenResponse](app/sap_client/docs/GenerateTokenResponse.md)
 - [LiveLinkResponse](app/sap_client/docs/LiveLinkResponse.md)
 - [MfaSoftToken](app/sap_client/docs/MfaSoftToken.md)
 - [MfaSoftTokenValidateResponse](app/sap_client/docs/MfaSoftTokenValidateResponse.md)
 - [PollMo](app/sap_client/docs/PollMo.md)
 - [PollMoResponse](app/sap_client/docs/PollMoResponse.md)
 - [PollStatus](app/sap_client/docs/PollStatus.md)
 - [PollStatusResponse](app/sap_client/docs/PollStatusResponse.md)
 - [SmsProperties](app/sap_client/docs/SmsProperties.md)
 - [SmsRequest](app/sap_client/docs/SmsRequest.md)
 - [SmsRequestV2](app/sap_client/docs/SmsRequestV2.md)
 - [SoftTokenRequest](app/sap_client/docs/SoftTokenRequest.md)
 - [SoftTokenValidateRequest](app/sap_client/docs/SoftTokenValidateRequest.md)
 - [UrlAuthResponse](app/sap_client/docs/UrlAuthResponse.md)
 - [UrlAuthorizationRequest](app/sap_client/docs/UrlAuthorizationRequest.md)
 - [ValidateSoftTokenRequest](app/sap_client/docs/ValidateSoftTokenRequest.md)
 - [ValidateTokenRequest](app/sap_client/docs/ValidateTokenRequest.md)
 - [ValidateTokenResponse](app/sap_client/docs/ValidateTokenResponse.md)


## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## OAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **livelink:api**: Grants access to interface with API endpoints
 - **livelink:pollData**: Grants read access to poll delivery statuses and MOs


## Author

sapdigitalinterconnect@sap.com

