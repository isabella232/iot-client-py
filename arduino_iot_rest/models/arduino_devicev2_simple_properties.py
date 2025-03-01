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


class ArduinoDevicev2SimpleProperties(object):
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
        'name': 'str',
        'updated_at': 'datetime',
        'value': 'object'
    }

    attribute_map = {
        'name': 'name',
        'updated_at': 'updated_at',
        'value': 'value'
    }

    def __init__(self, name=None, updated_at=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDevicev2SimpleProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._updated_at = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.updated_at = updated_at
        self.value = value

    @property
    def name(self):
        """Gets the name of this ArduinoDevicev2SimpleProperties.  # noqa: E501

        The name of the property  # noqa: E501

        :return: The name of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoDevicev2SimpleProperties.

        The name of the property  # noqa: E501

        :param name: The name of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this ArduinoDevicev2SimpleProperties.  # noqa: E501

        Update date of the property  # noqa: E501

        :return: The updated_at of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ArduinoDevicev2SimpleProperties.

        Update date of the property  # noqa: E501

        :param updated_at: The updated_at of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this ArduinoDevicev2SimpleProperties.  # noqa: E501

        Value of the property  # noqa: E501

        :return: The value of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ArduinoDevicev2SimpleProperties.

        Value of the property  # noqa: E501

        :param value: The value of this ArduinoDevicev2SimpleProperties.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, ArduinoDevicev2SimpleProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDevicev2SimpleProperties):
            return True

        return self.to_dict() != other.to_dict()
