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

class PoaPostData(object):
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
        'vcpu_cpu_map': 'list[PoaPostDataVcpuCpuMap]',
        'node_set': 'list[str]'
    }

    attribute_map = {
        'vcpu_cpu_map': 'vcpu_cpu_map',
        'node_set': 'node_set'
    }

    def __init__(self, vcpu_cpu_map=None, node_set=None):  # noqa: E501
        """PoaPostData - a model defined in Swagger"""  # noqa: E501
        self._vcpu_cpu_map = None
        self._node_set = None
        self.discriminator = None
        if vcpu_cpu_map is not None:
            self.vcpu_cpu_map = vcpu_cpu_map
        if node_set is not None:
            self.node_set = node_set

    @property
    def vcpu_cpu_map(self):
        """Gets the vcpu_cpu_map of this PoaPostData.  # noqa: E501


        :return: The vcpu_cpu_map of this PoaPostData.  # noqa: E501
        :rtype: list[PoaPostDataVcpuCpuMap]
        """
        return self._vcpu_cpu_map

    @vcpu_cpu_map.setter
    def vcpu_cpu_map(self, vcpu_cpu_map):
        """Sets the vcpu_cpu_map of this PoaPostData.


        :param vcpu_cpu_map: The vcpu_cpu_map of this PoaPostData.  # noqa: E501
        :type: list[PoaPostDataVcpuCpuMap]
        """

        self._vcpu_cpu_map = vcpu_cpu_map

    @property
    def node_set(self):
        """Gets the node_set of this PoaPostData.  # noqa: E501


        :return: The node_set of this PoaPostData.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_set

    @node_set.setter
    def node_set(self, node_set):
        """Sets the node_set of this PoaPostData.


        :param node_set: The node_set of this PoaPostData.  # noqa: E501
        :type: list[str]
        """

        self._node_set = node_set

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
        if issubclass(PoaPostData, dict):
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
        if not isinstance(other, PoaPostData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
