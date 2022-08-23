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
from fim.slivers.json import JSONSliver
from fim.slivers.network_node import NodeSliver
from fim.slivers.network_service import NetworkServiceSliver


class Sliver(object):
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
        'notice': 'str',
        'sliver_type': 'str',
        'sliver': 'object',
        'lease_start_time': 'str',
        'lease_end_time': 'str',
        'state': 'str',
        'pending_state': 'str',
        'join_state': 'str',
        'graph_node_id': 'str',
        'slice_id': 'str',
        'sliver_id': 'str'
    }

    attribute_map = {
        'notice': 'notice',
        'sliver_type': 'sliver_type',
        'sliver': 'sliver',
        'lease_start_time': 'lease_start_time',
        'lease_end_time': 'lease_end_time',
        'state': 'state',
        'pending_state': 'pending_state',
        'join_state': 'join_state',
        'graph_node_id': 'graph_node_id',
        'slice_id': 'slice_id',
        'sliver_id': 'sliver_id'
    }

    def __init__(self, notice=None, sliver_type=None, sliver=None, lease_start_time=None, lease_end_time=None, state=None, pending_state=None, join_state=None, graph_node_id=None, slice_id=None, sliver_id=None):  # noqa: E501
        """Sliver - a model defined in Swagger"""  # noqa: E501
        self._notice = None
        self._sliver_type = None
        self._sliver = None
        self._lease_start_time = None
        self._lease_end_time = None
        self._state = None
        self._pending_state = None
        self._join_state = None
        self._graph_node_id = None
        self._slice_id = None
        self._sliver_id = None
        self.discriminator = None
        if notice is not None:
            self.notice = notice
        if sliver_type is not None:
            self.sliver_type = sliver_type
        if sliver is not None:
            self.sliver = sliver
        if lease_start_time is not None:
            self.lease_start_time = lease_start_time
        if lease_end_time is not None:
            self.lease_end_time = lease_end_time
        if state is not None:
            self.state = state
        if pending_state is not None:
            self.pending_state = pending_state
        if join_state is not None:
            self.join_state = join_state
        self.graph_node_id = graph_node_id
        self.slice_id = slice_id
        self.sliver_id = sliver_id

    @property
    def notice(self):
        """Gets the notice of this Sliver.  # noqa: E501


        :return: The notice of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        """Sets the notice of this Sliver.


        :param notice: The notice of this Sliver.  # noqa: E501
        :type: str
        """

        self._notice = notice

    @property
    def sliver_type(self):
        """Gets the sliver_type of this Sliver.  # noqa: E501


        :return: The sliver_type of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._sliver_type

    @sliver_type.setter
    def sliver_type(self, sliver_type):
        """Sets the sliver_type of this Sliver.


        :param sliver_type: The sliver_type of this Sliver.  # noqa: E501
        :type: str
        """

        self._sliver_type = sliver_type

    @property
    def sliver(self):
        """Gets the sliver of this Sliver.  # noqa: E501


        :return: The sliver of this Sliver.  # noqa: E501
        :rtype: NodeSliver or NetworkServiceSliver
        """
        if self._sliver is not None:
            if self.sliver_type == NodeSliver.__name__:
                return JSONSliver.node_sliver_from_json(s=self._sliver)
            elif self.sliver_type == NetworkServiceSliver.__name__:
                return JSONSliver.network_service_sliver_from_json(s=self._sliver)

        return self._sliver

    @sliver.setter
    def sliver(self, sliver):
        """Sets the sliver of this Sliver.


        :param sliver: The sliver of this Sliver.  # noqa: E501
        :type: object
        """

        self._sliver = sliver

    @property
    def lease_start_time(self):
        """Gets the lease_start_time of this Sliver.  # noqa: E501


        :return: The lease_start_time of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._lease_start_time

    @lease_start_time.setter
    def lease_start_time(self, lease_start_time):
        """Sets the lease_start_time of this Sliver.


        :param lease_start_time: The lease_start_time of this Sliver.  # noqa: E501
        :type: str
        """

        self._lease_start_time = lease_start_time

    @property
    def lease_end_time(self):
        """Gets the lease_end_time of this Sliver.  # noqa: E501


        :return: The lease_end_time of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._lease_end_time

    @lease_end_time.setter
    def lease_end_time(self, lease_end_time):
        """Sets the lease_end_time of this Sliver.


        :param lease_end_time: The lease_end_time of this Sliver.  # noqa: E501
        :type: str
        """

        self._lease_end_time = lease_end_time

    @property
    def state(self):
        """Gets the state of this Sliver.  # noqa: E501


        :return: The state of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Sliver.


        :param state: The state of this Sliver.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def pending_state(self):
        """Gets the pending_state of this Sliver.  # noqa: E501


        :return: The pending_state of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._pending_state

    @pending_state.setter
    def pending_state(self, pending_state):
        """Sets the pending_state of this Sliver.


        :param pending_state: The pending_state of this Sliver.  # noqa: E501
        :type: str
        """

        self._pending_state = pending_state

    @property
    def join_state(self):
        """Gets the join_state of this Sliver.  # noqa: E501


        :return: The join_state of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._join_state

    @join_state.setter
    def join_state(self, join_state):
        """Sets the join_state of this Sliver.


        :param join_state: The join_state of this Sliver.  # noqa: E501
        :type: str
        """

        self._join_state = join_state

    @property
    def graph_node_id(self):
        """Gets the graph_node_id of this Sliver.  # noqa: E501


        :return: The graph_node_id of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._graph_node_id

    @graph_node_id.setter
    def graph_node_id(self, graph_node_id):
        """Sets the graph_node_id of this Sliver.


        :param graph_node_id: The graph_node_id of this Sliver.  # noqa: E501
        :type: str
        """
        if graph_node_id is None:
            raise ValueError("Invalid value for `graph_node_id`, must not be `None`")  # noqa: E501

        self._graph_node_id = graph_node_id

    @property
    def slice_id(self):
        """Gets the slice_id of this Sliver.  # noqa: E501


        :return: The slice_id of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._slice_id

    @slice_id.setter
    def slice_id(self, slice_id):
        """Sets the slice_id of this Sliver.


        :param slice_id: The slice_id of this Sliver.  # noqa: E501
        :type: str
        """
        if slice_id is None:
            raise ValueError("Invalid value for `slice_id`, must not be `None`")  # noqa: E501

        self._slice_id = slice_id

    @property
    def sliver_id(self):
        """Gets the sliver_id of this Sliver.  # noqa: E501


        :return: The sliver_id of this Sliver.  # noqa: E501
        :rtype: str
        """
        return self._sliver_id

    @sliver_id.setter
    def sliver_id(self, sliver_id):
        """Sets the sliver_id of this Sliver.


        :param sliver_id: The sliver_id of this Sliver.  # noqa: E501
        :type: str
        """
        if sliver_id is None:
            raise ValueError("Invalid value for `sliver_id`, must not be `None`")  # noqa: E501

        self._sliver_id = sliver_id

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
<<<<<<< HEAD
            elif isinstance(value, NodeSliver) or isinstance(value, NetworkServiceSliver):
                result[attr] = JSONSliver.sliver_to_json(sliver=value)
=======
>>>>>>> a99acea78648e749db8881a5988f744ec3e5ba18
            else:
                result[attr] = value
        if issubclass(Sliver, dict):
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
        if not isinstance(other, Sliver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
