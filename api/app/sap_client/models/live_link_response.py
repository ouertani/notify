# coding: utf-8

"""
    SAP Digital Interconnect LiveLink 365

    The SAP Live Link 365 is a communication platform as a service (CPaaS) that leverages robust delivery technology, SAP’s global relationships, and the power of SAP’s Cloud Platform to provide affordable, scalable, and global messaging solutions for best in class SMS management.  # noqa: E501

    The version of the OpenAPI document: v1.1.0
    Contact: sapdigitalinterconnect@sap.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from app.sap_client.configuration import Configuration


class LiveLinkResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_error_code': 'int',
        'debug_message': 'str',
        'doc_url': 'str',
        'http_status_code': 'str',
        'livelink_order_ids': 'list[DestOrderId]',
        'user_message': 'str'
    }

    attribute_map = {
        'api_error_code': 'apiErrorCode',
        'debug_message': 'debugMessage',
        'doc_url': 'docUrl',
        'http_status_code': 'httpStatusCode',
        'livelink_order_ids': 'livelinkOrderIds',
        'user_message': 'userMessage'
    }

    def __init__(self, api_error_code=None, debug_message=None, doc_url=None, http_status_code=None, livelink_order_ids=None, user_message=None, local_vars_configuration=None):  # noqa: E501
        """LiveLinkResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_error_code = None
        self._debug_message = None
        self._doc_url = None
        self._http_status_code = None
        self._livelink_order_ids = None
        self._user_message = None
        self.discriminator = None

        if api_error_code is not None:
            self.api_error_code = api_error_code
        if debug_message is not None:
            self.debug_message = debug_message
        if doc_url is not None:
            self.doc_url = doc_url
        if http_status_code is not None:
            self.http_status_code = http_status_code
        if livelink_order_ids is not None:
            self.livelink_order_ids = livelink_order_ids
        if user_message is not None:
            self.user_message = user_message

    @property
    def api_error_code(self):
        """Gets the api_error_code of this LiveLinkResponse.  # noqa: E501

        Internal error code, present only if error occurs.  # noqa: E501

        :return: The api_error_code of this LiveLinkResponse.  # noqa: E501
        :rtype: int
        """
        return self._api_error_code

    @api_error_code.setter
    def api_error_code(self, api_error_code):
        """Sets the api_error_code of this LiveLinkResponse.

        Internal error code, present only if error occurs.  # noqa: E501

        :param api_error_code: The api_error_code of this LiveLinkResponse.  # noqa: E501
        :type: int
        """

        self._api_error_code = api_error_code

    @property
    def debug_message(self):
        """Gets the debug_message of this LiveLinkResponse.  # noqa: E501

        Debug message describing the problem, present only if error occurs.  # noqa: E501

        :return: The debug_message of this LiveLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._debug_message

    @debug_message.setter
    def debug_message(self, debug_message):
        """Sets the debug_message of this LiveLinkResponse.

        Debug message describing the problem, present only if error occurs.  # noqa: E501

        :param debug_message: The debug_message of this LiveLinkResponse.  # noqa: E501
        :type: str
        """

        self._debug_message = debug_message

    @property
    def doc_url(self):
        """Gets the doc_url of this LiveLinkResponse.  # noqa: E501

        Unique locator for the doc generated in relation to the request.  # noqa: E501

        :return: The doc_url of this LiveLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._doc_url

    @doc_url.setter
    def doc_url(self, doc_url):
        """Sets the doc_url of this LiveLinkResponse.

        Unique locator for the doc generated in relation to the request.  # noqa: E501

        :param doc_url: The doc_url of this LiveLinkResponse.  # noqa: E501
        :type: str
        """

        self._doc_url = doc_url

    @property
    def http_status_code(self):
        """Gets the http_status_code of this LiveLinkResponse.  # noqa: E501

        HTTP status code returned by API Gateway.  # noqa: E501

        :return: The http_status_code of this LiveLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this LiveLinkResponse.

        HTTP status code returned by API Gateway.  # noqa: E501

        :param http_status_code: The http_status_code of this LiveLinkResponse.  # noqa: E501
        :type: str
        """

        self._http_status_code = http_status_code

    @property
    def livelink_order_ids(self):
        """Gets the livelink_order_ids of this LiveLinkResponse.  # noqa: E501

        List of all mobile numbers to which message is sent along with list of all order IDs when sent data is processed successfully.  # noqa: E501

        :return: The livelink_order_ids of this LiveLinkResponse.  # noqa: E501
        :rtype: list[DestOrderId]
        """
        return self._livelink_order_ids

    @livelink_order_ids.setter
    def livelink_order_ids(self, livelink_order_ids):
        """Sets the livelink_order_ids of this LiveLinkResponse.

        List of all mobile numbers to which message is sent along with list of all order IDs when sent data is processed successfully.  # noqa: E501

        :param livelink_order_ids: The livelink_order_ids of this LiveLinkResponse.  # noqa: E501
        :type: list[DestOrderId]
        """

        self._livelink_order_ids = livelink_order_ids

    @property
    def user_message(self):
        """Gets the user_message of this LiveLinkResponse.  # noqa: E501

        The error message describing the problem, present only if error occurs.  # noqa: E501

        :return: The user_message of this LiveLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """Sets the user_message of this LiveLinkResponse.

        The error message describing the problem, present only if error occurs.  # noqa: E501

        :param user_message: The user_message of this LiveLinkResponse.  # noqa: E501
        :type: str
        """

        self._user_message = user_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LiveLinkResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LiveLinkResponse):
            return True

        return self.to_dict() != other.to_dict()