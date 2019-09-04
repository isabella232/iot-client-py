# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Error(object):
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
        'code': 'str',
        'detail': 'str',
        'id': 'str',
        'meta': 'dict(str, object)',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'detail': 'detail',
        'id': 'id',
        'meta': 'meta',
        'status': 'status'
    }

    def __init__(self, code=None, detail=None, id=None, meta=None, status=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._detail = None
        self._id = None
        self._meta = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        if id is not None:
            self.id = id
        if meta is not None:
            self.meta = meta
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501

        an application-specific error code, expressed as a string value.  # noqa: E501

        :return: The code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        an application-specific error code, expressed as a string value.  # noqa: E501

        :param code: The code of this Error.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error.  # noqa: E501

        a human-readable explanation specific to this occurrence of the problem.  # noqa: E501

        :return: The detail of this Error.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        a human-readable explanation specific to this occurrence of the problem.  # noqa: E501

        :param detail: The detail of this Error.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def id(self):
        """Gets the id of this Error.  # noqa: E501

        a unique identifier for this particular occurrence of the problem.  # noqa: E501

        :return: The id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Error.

        a unique identifier for this particular occurrence of the problem.  # noqa: E501

        :param id: The id of this Error.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this Error.  # noqa: E501

        a meta object containing non-standard meta-information about the error.  # noqa: E501

        :return: The meta of this Error.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Error.

        a meta object containing non-standard meta-information about the error.  # noqa: E501

        :param meta: The meta of this Error.  # noqa: E501
        :type: dict(str, object)
        """

        self._meta = meta

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501

        the HTTP status code applicable to this problem, expressed as a string value.  # noqa: E501

        :return: The status of this Error.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.

        the HTTP status code applicable to this problem, expressed as a string value.  # noqa: E501

        :param status: The status of this Error.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
