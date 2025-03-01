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


class Widget(object):
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
        'height': 'int',
        'height_mobile': 'int',
        'id': 'str',
        'name': 'str',
        'options': 'dict(str, object)',
        'type': 'str',
        'variables': 'list[str]',
        'width': 'int',
        'width_mobile': 'int',
        'x': 'int',
        'x_mobile': 'int',
        'y': 'int',
        'y_mobile': 'int'
    }

    attribute_map = {
        'height': 'height',
        'height_mobile': 'height_mobile',
        'id': 'id',
        'name': 'name',
        'options': 'options',
        'type': 'type',
        'variables': 'variables',
        'width': 'width',
        'width_mobile': 'width_mobile',
        'x': 'x',
        'x_mobile': 'x_mobile',
        'y': 'y',
        'y_mobile': 'y_mobile'
    }

    def __init__(self, height=None, height_mobile=None, id=None, name=None, options=None, type=None, variables=None, width=None, width_mobile=None, x=None, x_mobile=None, y=None, y_mobile=None, local_vars_configuration=None):  # noqa: E501
        """Widget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._height = None
        self._height_mobile = None
        self._id = None
        self._name = None
        self._options = None
        self._type = None
        self._variables = None
        self._width = None
        self._width_mobile = None
        self._x = None
        self._x_mobile = None
        self._y = None
        self._y_mobile = None
        self.discriminator = None

        self.height = height
        if height_mobile is not None:
            self.height_mobile = height_mobile
        self.id = id
        if name is not None:
            self.name = name
        self.options = options
        self.type = type
        if variables is not None:
            self.variables = variables
        self.width = width
        if width_mobile is not None:
            self.width_mobile = width_mobile
        self.x = x
        if x_mobile is not None:
            self.x_mobile = x_mobile
        self.y = y
        if y_mobile is not None:
            self.y_mobile = y_mobile

    @property
    def height(self):
        """Gets the height of this Widget.  # noqa: E501

        Widget current height for desktop  # noqa: E501

        :return: The height of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Widget.

        Widget current height for desktop  # noqa: E501

        :param height: The height of this Widget.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def height_mobile(self):
        """Gets the height_mobile of this Widget.  # noqa: E501

        Widget current height for mobile  # noqa: E501

        :return: The height_mobile of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._height_mobile

    @height_mobile.setter
    def height_mobile(self, height_mobile):
        """Sets the height_mobile of this Widget.

        Widget current height for mobile  # noqa: E501

        :param height_mobile: The height_mobile of this Widget.  # noqa: E501
        :type: int
        """

        self._height_mobile = height_mobile

    @property
    def id(self):
        """Gets the id of this Widget.  # noqa: E501

        The UUID of the widget, set by client  # noqa: E501

        :return: The id of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Widget.

        The UUID of the widget, set by client  # noqa: E501

        :param id: The id of this Widget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Widget.  # noqa: E501

        The name of the widget  # noqa: E501

        :return: The name of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Widget.

        The name of the widget  # noqa: E501

        :param name: The name of this Widget.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this Widget.  # noqa: E501

        Widget options  # noqa: E501

        :return: The options of this Widget.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Widget.

        Widget options  # noqa: E501

        :param options: The options of this Widget.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def type(self):
        """Gets the type of this Widget.  # noqa: E501

        The type of the widget  # noqa: E501

        :return: The type of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Widget.

        The type of the widget  # noqa: E501

        :param type: The type of this Widget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def variables(self):
        """Gets the variables of this Widget.  # noqa: E501


        :return: The variables of this Widget.  # noqa: E501
        :rtype: list[str]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this Widget.


        :param variables: The variables of this Widget.  # noqa: E501
        :type: list[str]
        """

        self._variables = variables

    @property
    def width(self):
        """Gets the width of this Widget.  # noqa: E501

        Widget current width for desktop  # noqa: E501

        :return: The width of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Widget.

        Widget current width for desktop  # noqa: E501

        :param width: The width of this Widget.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def width_mobile(self):
        """Gets the width_mobile of this Widget.  # noqa: E501

        Widget current width for mobile  # noqa: E501

        :return: The width_mobile of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._width_mobile

    @width_mobile.setter
    def width_mobile(self, width_mobile):
        """Sets the width_mobile of this Widget.

        Widget current width for mobile  # noqa: E501

        :param width_mobile: The width_mobile of this Widget.  # noqa: E501
        :type: int
        """

        self._width_mobile = width_mobile

    @property
    def x(self):
        """Gets the x of this Widget.  # noqa: E501

        Widget x position for desktop  # noqa: E501

        :return: The x of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Widget.

        Widget x position for desktop  # noqa: E501

        :param x: The x of this Widget.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and x is None:  # noqa: E501
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def x_mobile(self):
        """Gets the x_mobile of this Widget.  # noqa: E501

        Widget x position for mobile  # noqa: E501

        :return: The x_mobile of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._x_mobile

    @x_mobile.setter
    def x_mobile(self, x_mobile):
        """Sets the x_mobile of this Widget.

        Widget x position for mobile  # noqa: E501

        :param x_mobile: The x_mobile of this Widget.  # noqa: E501
        :type: int
        """

        self._x_mobile = x_mobile

    @property
    def y(self):
        """Gets the y of this Widget.  # noqa: E501

        Widget y position for desktop  # noqa: E501

        :return: The y of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Widget.

        Widget y position for desktop  # noqa: E501

        :param y: The y of this Widget.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and y is None:  # noqa: E501
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def y_mobile(self):
        """Gets the y_mobile of this Widget.  # noqa: E501

        Widget y position for mobile  # noqa: E501

        :return: The y_mobile of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._y_mobile

    @y_mobile.setter
    def y_mobile(self, y_mobile):
        """Sets the y_mobile of this Widget.

        Widget y position for mobile  # noqa: E501

        :param y_mobile: The y_mobile of this Widget.  # noqa: E501
        :type: int
        """

        self._y_mobile = y_mobile

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
        if not isinstance(other, Widget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Widget):
            return True

        return self.to_dict() != other.to_dict()
