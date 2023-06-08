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

class PoaPost(object):
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
        'operation': 'str',
        'data': 'PoaPostData'
    }

    attribute_map = {
        'operation': 'operation',
        'data': 'data'
    }

    def __init__(self, operation=None, data=None):  # noqa: E501
        """PoaPost - a model defined in Swagger"""  # noqa: E501
        self._operation = None
        self._data = None
        self.discriminator = None
        self.operation = operation
        if data is not None:
            self.data = data

    @property
    def operation(self):
        """Gets the operation of this PoaPost.  # noqa: E501


        :return: The operation of this PoaPost.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PoaPost.


        :param operation: The operation of this PoaPost.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["cpuinfo", "numainfo", "cpupin", "numatune", "reboot"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def data(self):
        """Gets the data of this PoaPost.  # noqa: E501


        :return: The data of this PoaPost.  # noqa: E501
        :rtype: PoaPostData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PoaPost.


        :param data: The data of this PoaPost.  # noqa: E501
        :type: PoaPostData
        """

        self._data = data

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
        if issubclass(PoaPost, dict):
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
        if not isinstance(other, PoaPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
