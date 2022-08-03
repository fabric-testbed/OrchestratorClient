# coding: utf-8

"""
    Fabric Orchestrator API

    This is Fabric Orchestrator API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Status401Unauthorized(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'errors': 'list[Status401UnauthorizedErrors]',
        'type': 'str',
        'size': 'int',
        'status': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'type': 'type',
        'size': 'size',
        'status': 'status'
    }

    def __init__(self, errors=None, type='error', size=1, status=401):  # noqa: E501
        """Status401Unauthorized - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._type = None
        self._size = None
        self._status = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status

    @property
    def errors(self):
        """Gets the errors of this Status401Unauthorized.  # noqa: E501


        :return: The errors of this Status401Unauthorized.  # noqa: E501
        :rtype: list[Status401UnauthorizedErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Status401Unauthorized.


        :param errors: The errors of this Status401Unauthorized.  # noqa: E501
        :type: list[Status401UnauthorizedErrors]
        """

        self._errors = errors

    @property
    def type(self):
        """Gets the type of this Status401Unauthorized.  # noqa: E501


        :return: The type of this Status401Unauthorized.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Status401Unauthorized.


        :param type: The type of this Status401Unauthorized.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def size(self):
        """Gets the size of this Status401Unauthorized.  # noqa: E501


        :return: The size of this Status401Unauthorized.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Status401Unauthorized.


        :param size: The size of this Status401Unauthorized.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def status(self):
        """Gets the status of this Status401Unauthorized.  # noqa: E501


        :return: The status of this Status401Unauthorized.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Status401Unauthorized.


        :param status: The status of this Status401Unauthorized.  # noqa: E501
        :type: int
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Status401Unauthorized, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Status401Unauthorized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
