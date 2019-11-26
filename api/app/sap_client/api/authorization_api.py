# coding: utf-8

"""
    SAP Digital Interconnect LiveLink 365

    The SAP Live Link 365 is a communication platform as a service (CPaaS) that leverages robust delivery technology, SAP’s global relationships, and the power of SAP’s Cloud Platform to provide affordable, scalable, and global messaging solutions for best in class SMS management.  # noqa: E501

    The version of the OpenAPI document: v1.1.0
    Contact: sapdigitalinterconnect@sap.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from app.sap_client.api_client import ApiClient
from app.sap_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class AuthorizationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def token_authorization_using_post1(self, grant_type, **kwargs):  # noqa: E501
        """Request Authorization  # noqa: E501

        Returns an OAuth2 bearer token in exchange for the client credentials provided as parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.token_authorization_using_post1(grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type: The grant type should be **client_credentials** to receive an access token. This access token is valid for 45 minutes. The grant type can be 'refresh_token' in subsequent API calls in order to refresh the access token before it expires. (required)
        :param str refresh_token: Refresh token that was received along with the access token in response to a previous request to this endpoint. The refresh token is valid for 60 minutes. It can be used in subsequent requests to this endpoint, along with **'grant_type' set as 'refresh_token'**, to get a new access token (after the previous token's 45-minute lifetime is over) without having to provide client credentials again.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.token_authorization_using_post1_with_http_info(grant_type, **kwargs)  # noqa: E501

    def token_authorization_using_post1_with_http_info(self, grant_type, **kwargs):  # noqa: E501
        """Request Authorization  # noqa: E501

        Returns an OAuth2 bearer token in exchange for the client credentials provided as parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.token_authorization_using_post1_with_http_info(grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type: The grant type should be **client_credentials** to receive an access token. This access token is valid for 45 minutes. The grant type can be 'refresh_token' in subsequent API calls in order to refresh the access token before it expires. (required)
        :param str refresh_token: Refresh token that was received along with the access token in response to a previous request to this endpoint. The refresh token is valid for 60 minutes. It can be used in subsequent requests to this endpoint, along with **'grant_type' set as 'refresh_token'**, to get a new access token (after the previous token's 45-minute lifetime is over) without having to provide client credentials again.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessToken, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['grant_type', 'refresh_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method token_authorization_using_post1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'grant_type' is set
        if self.api_client.client_side_validation and ('grant_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['grant_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `grant_type` when calling `token_authorization_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in local_var_params:
            form_params.append(('grant_type', local_var_params['grant_type']))  # noqa: E501
        if 'refresh_token' in local_var_params:
            form_params.append(('refresh_token', local_var_params['refresh_token']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_using_post1(self, access_token, **kwargs):  # noqa: E501
        """Validate Authorization  # noqa: E501

        Determines whether the token given as parameter is still valid for authorization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_using_post1(access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str access_token: The token to be validated (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.validate_using_post1_with_http_info(access_token, **kwargs)  # noqa: E501

    def validate_using_post1_with_http_info(self, access_token, **kwargs):  # noqa: E501
        """Validate Authorization  # noqa: E501

        Determines whether the token given as parameter is still valid for authorization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_using_post1_with_http_info(access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str access_token: The token to be validated (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_using_post1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'access_token' is set
        if self.api_client.client_side_validation and ('access_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['access_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_token` when calling `validate_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'access_token' in local_var_params:
            body_params = local_var_params['access_token']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
