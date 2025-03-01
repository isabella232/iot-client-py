# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class Dashboardshare(object):
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
        'user_id': 'str',
        'username': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'username': 'username'
    }

    def __init__(self, user_id=None, username=None, local_vars_configuration=None):  # noqa: E501
        """Dashboardshare - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._username = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username

    @property
    def user_id(self):
        """Gets the user_id of this Dashboardshare.  # noqa: E501

        The userID of the user you want to share the dashboard with  # noqa: E501

        :return: The user_id of this Dashboardshare.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Dashboardshare.

        The userID of the user you want to share the dashboard with  # noqa: E501

        :param user_id: The user_id of this Dashboardshare.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this Dashboardshare.  # noqa: E501

        The username of the user you want to share the dashboard with  # noqa: E501

        :return: The username of this Dashboardshare.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Dashboardshare.

        The username of the user you want to share the dashboard with  # noqa: E501

        :param username: The username of this Dashboardshare.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, Dashboardshare):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dashboardshare):
            return True

        return self.to_dict() != other.to_dict()
