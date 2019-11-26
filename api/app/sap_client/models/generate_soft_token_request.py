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


class GenerateSoftTokenRequest(object):
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
        'account_id': 'int',
        'telephone_number': 'int',
        'message_body': 'str',
        'character_set': 'str',
        'token_length': 'int',
        'pin_type': 'int',
        'time_out': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'telephone_number': 'telephoneNumber',
        'message_body': 'messageBody',
        'character_set': 'characterSet',
        'token_length': 'tokenLength',
        'pin_type': 'pinType',
        'time_out': 'timeOut'
    }

    def __init__(self, account_id=None, telephone_number=None, message_body=None, character_set=None, token_length=None, pin_type=None, time_out=None, local_vars_configuration=None):  # noqa: E501
        """GenerateSoftTokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._telephone_number = None
        self._message_body = None
        self._character_set = None
        self._token_length = None
        self._pin_type = None
        self._time_out = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if telephone_number is not None:
            self.telephone_number = telephone_number
        if message_body is not None:
            self.message_body = message_body
        if character_set is not None:
            self.character_set = character_set
        if token_length is not None:
            self.token_length = token_length
        if pin_type is not None:
            self.pin_type = pin_type
        if time_out is not None:
            self.time_out = time_out

    @property
    def account_id(self):
        """Gets the account_id of this GenerateSoftTokenRequest.  # noqa: E501

        The System account that will have access to send messages through the HUB Account. This is the MFA Account ID.  # noqa: E501

        :return: The account_id of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GenerateSoftTokenRequest.

        The System account that will have access to send messages through the HUB Account. This is the MFA Account ID.  # noqa: E501

        :param account_id: The account_id of this GenerateSoftTokenRequest.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def telephone_number(self):
        """Gets the telephone_number of this GenerateSoftTokenRequest.  # noqa: E501

        The user phone number that will receive the token.  # noqa: E501

        :return: The telephone_number of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        """Sets the telephone_number of this GenerateSoftTokenRequest.

        The user phone number that will receive the token.  # noqa: E501

        :param telephone_number: The telephone_number of this GenerateSoftTokenRequest.  # noqa: E501
        :type: int
        """

        self._telephone_number = telephone_number

    @property
    def message_body(self):
        """Gets the message_body of this GenerateSoftTokenRequest.  # noqa: E501

        The message that will be carried over with the token.  # noqa: E501

        :return: The message_body of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this GenerateSoftTokenRequest.

        The message that will be carried over with the token.  # noqa: E501

        :param message_body: The message_body of this GenerateSoftTokenRequest.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def character_set(self):
        """Gets the character_set of this GenerateSoftTokenRequest.  # noqa: E501

        It is the Message Character set.  # noqa: E501

        :return: The character_set of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this GenerateSoftTokenRequest.

        It is the Message Character set.  # noqa: E501

        :param character_set: The character_set of this GenerateSoftTokenRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["8b", "BIG5", "UTF8", "GB2312", "8859-7", "BIG5 and UCS2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and character_set not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `character_set` ({0}), must be one of {1}"  # noqa: E501
                .format(character_set, allowed_values)
            )

        self._character_set = character_set

    @property
    def token_length(self):
        """Gets the token_length of this GenerateSoftTokenRequest.  # noqa: E501

        Length of characters from Minimum 4 to a Maximum of 9.  # noqa: E501

        :return: The token_length of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._token_length

    @token_length.setter
    def token_length(self, token_length):
        """Sets the token_length of this GenerateSoftTokenRequest.

        Length of characters from Minimum 4 to a Maximum of 9.  # noqa: E501

        :param token_length: The token_length of this GenerateSoftTokenRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                token_length is not None and token_length > 9):  # noqa: E501
            raise ValueError("Invalid value for `token_length`, must be a value less than or equal to `9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token_length is not None and token_length < 4):  # noqa: E501
            raise ValueError("Invalid value for `token_length`, must be a value greater than or equal to `4`")  # noqa: E501

        self._token_length = token_length

    @property
    def pin_type(self):
        """Gets the pin_type of this GenerateSoftTokenRequest.  # noqa: E501

        Type of PIN. 0 for Numeric and 1 for Alphanumeric.  # noqa: E501

        :return: The pin_type of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        """Sets the pin_type of this GenerateSoftTokenRequest.

        Type of PIN. 0 for Numeric and 1 for Alphanumeric.  # noqa: E501

        :param pin_type: The pin_type of this GenerateSoftTokenRequest.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pin_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pin_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pin_type, allowed_values)
            )

        self._pin_type = pin_type

    @property
    def time_out(self):
        """Gets the time_out of this GenerateSoftTokenRequest.  # noqa: E501

        How long the generated token will be valid in seconds. Minimum of 30 to a Maximum of 900. For Example: 300  # noqa: E501

        :return: The time_out of this GenerateSoftTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._time_out

    @time_out.setter
    def time_out(self, time_out):
        """Sets the time_out of this GenerateSoftTokenRequest.

        How long the generated token will be valid in seconds. Minimum of 30 to a Maximum of 900. For Example: 300  # noqa: E501

        :param time_out: The time_out of this GenerateSoftTokenRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time_out is not None and time_out > 900):  # noqa: E501
            raise ValueError("Invalid value for `time_out`, must be a value less than or equal to `900`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_out is not None and time_out < 30):  # noqa: E501
            raise ValueError("Invalid value for `time_out`, must be a value greater than or equal to `30`")  # noqa: E501

        self._time_out = time_out

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
        if not isinstance(other, GenerateSoftTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateSoftTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
