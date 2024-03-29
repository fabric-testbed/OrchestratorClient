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

class SlicesPost(object):
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
        'graph_model': 'str',
        'ssh_keys': 'list[str]'
    }

    attribute_map = {
        'graph_model': 'graph_model',
        'ssh_keys': 'ssh_keys'
    }

    def __init__(self, graph_model=None, ssh_keys=None):  # noqa: E501
        """SlicesPost - a model defined in Swagger"""  # noqa: E501
        self._graph_model = None
        self._ssh_keys = None
        self.discriminator = None
        self.graph_model = graph_model
        self.ssh_keys = ssh_keys

    @property
    def graph_model(self):
        """Gets the graph_model of this SlicesPost.  # noqa: E501


        :return: The graph_model of this SlicesPost.  # noqa: E501
        :rtype: str
        """
        return self._graph_model

    @graph_model.setter
    def graph_model(self, graph_model):
        """Sets the graph_model of this SlicesPost.


        :param graph_model: The graph_model of this SlicesPost.  # noqa: E501
        :type: str
        """
        if graph_model is None:
            raise ValueError("Invalid value for `graph_model`, must not be `None`")  # noqa: E501

        self._graph_model = graph_model

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this SlicesPost.  # noqa: E501


        :return: The ssh_keys of this SlicesPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this SlicesPost.


        :param ssh_keys: The ssh_keys of this SlicesPost.  # noqa: E501
        :type: list[str]
        """
        if ssh_keys is None:
            raise ValueError("Invalid value for `ssh_keys`, must not be `None`")  # noqa: E501

        self._ssh_keys = ssh_keys

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
        if issubclass(SlicesPost, dict):
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
        if not isinstance(other, SlicesPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
