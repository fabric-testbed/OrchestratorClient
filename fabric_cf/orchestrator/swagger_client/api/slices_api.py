# coding: utf-8

"""
    Fabric Orchestrator API

    This is Fabric Orchestrator API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fabric_cf.orchestrator.swagger_client.api_client import ApiClient


class SlicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def slices_create_post(self, body, slice_name, ssh_key, **kwargs):  # noqa: E501
        """Create slice  # noqa: E501

        Request to create slice as described in the request. Request would be a graph ML describing the requested resources. Resources may be requested to be created now or in future. On success, one or more slivers are allocated, containing resources satisfying the request, and assigned to the given slice. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of these resources asynchronously on the appropriate sites either now or in the future as requested. Experimenter can invoke get slice API to get the latest state of the requested resources.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_create_post(body, slice_name, ssh_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slice_name: Slice Name (required)
        :param str ssh_key: User SSH Key (required)
        :param str lease_end_time: Lease End Time for the Slice
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_create_post_with_http_info(body, slice_name, ssh_key, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_create_post_with_http_info(body, slice_name, ssh_key, **kwargs)  # noqa: E501
            return data

    def slices_create_post_with_http_info(self, body, slice_name, ssh_key, **kwargs):  # noqa: E501
        """Create slice  # noqa: E501

        Request to create slice as described in the request. Request would be a graph ML describing the requested resources. Resources may be requested to be created now or in future. On success, one or more slivers are allocated, containing resources satisfying the request, and assigned to the given slice. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of these resources asynchronously on the appropriate sites either now or in the future as requested. Experimenter can invoke get slice API to get the latest state of the requested resources.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_create_post_with_http_info(body, slice_name, ssh_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slice_name: Slice Name (required)
        :param str ssh_key: User SSH Key (required)
        :param str lease_end_time: Lease End Time for the Slice
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slice_name', 'ssh_key', 'lease_end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_create_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slices_create_post`")  # noqa: E501
        # verify the required parameter 'slice_name' is set
        if ('slice_name' not in params or
                params['slice_name'] is None):
            raise ValueError("Missing the required parameter `slice_name` when calling `slices_create_post`")  # noqa: E501
        # verify the required parameter 'ssh_key' is set
        if ('ssh_key' not in params or
                params['ssh_key'] is None):
            raise ValueError("Missing the required parameter `ssh_key` when calling `slices_create_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'slice_name' in params:
            query_params.append(('sliceName', params['slice_name']))  # noqa: E501
        if 'ssh_key' in params:
            query_params.append(('sshKey', params['ssh_key']))  # noqa: E501
        if 'lease_end_time' in params:
            query_params.append(('leaseEndTime', params['lease_end_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_delete_slice_id_delete(self, slice_id, **kwargs):  # noqa: E501
        """Delete slice.  # noqa: E501

        Request to delete slice. On success, resources associated with slice or sliver are stopped if necessary, de-provisioned and un-allocated at the respective sites.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_delete_slice_id_delete(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_delete_slice_id_delete_with_http_info(slice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_delete_slice_id_delete_with_http_info(slice_id, **kwargs)  # noqa: E501
            return data

    def slices_delete_slice_id_delete_with_http_info(self, slice_id, **kwargs):  # noqa: E501
        """Delete slice.  # noqa: E501

        Request to delete slice. On success, resources associated with slice or sliver are stopped if necessary, de-provisioned and un-allocated at the respective sites.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_delete_slice_id_delete_with_http_info(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_delete_slice_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_delete_slice_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/delete/{sliceID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_get(self, state, **kwargs):  # noqa: E501
        """Retrieve a listing of user slices  # noqa: E501

        Retrieve a listing of user slices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_get(state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: Slice state (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_get_with_http_info(state, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_get_with_http_info(state, **kwargs)  # noqa: E501
            return data

    def slices_get_with_http_info(self, state, **kwargs):  # noqa: E501
        """Retrieve a listing of user slices  # noqa: E501

        Retrieve a listing of user slices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_get_with_http_info(state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: Slice state (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `slices_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_modify_slice_id_put(self, body, slice_id, **kwargs):  # noqa: E501
        """Modify slice  # noqa: E501

        Request to modify slice as described in the request. Request would be a Graph ML describing the requested resources for slice or a dictionary for sliver. On success, for one or more slivers are modified. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of the new resources on the appropriate sites either now or in the future based as requested. Modify operations may include add/delete/modify a container/VM/Baremetal server/network or other resources to the slice.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_modify_slice_id_put(body, slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_modify_slice_id_put_with_http_info(body, slice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_modify_slice_id_put_with_http_info(body, slice_id, **kwargs)  # noqa: E501
            return data

    def slices_modify_slice_id_put_with_http_info(self, body, slice_id, **kwargs):  # noqa: E501
        """Modify slice  # noqa: E501

        Request to modify slice as described in the request. Request would be a Graph ML describing the requested resources for slice or a dictionary for sliver. On success, for one or more slivers are modified. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of the new resources on the appropriate sites either now or in the future based as requested. Modify operations may include add/delete/modify a container/VM/Baremetal server/network or other resources to the slice.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_modify_slice_id_put_with_http_info(body, slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'slice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_modify_slice_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `slices_modify_slice_id_put`")  # noqa: E501
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_modify_slice_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/modify/{sliceID}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_redeem_slice_id_post(self, slice_id, **kwargs):  # noqa: E501
        """Redeem resources reserved via Create API  # noqa: E501

        Request that the reserved resources be made provisioned, instantiating or otherwise realizing the resources, such that they have a valid operational status and may possibly be made ready for experimenter use. This operation is synchronous, but may start a longer process, such as creating and imaging a virtual machine.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_redeem_slice_id_post(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_redeem_slice_id_post_with_http_info(slice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_redeem_slice_id_post_with_http_info(slice_id, **kwargs)  # noqa: E501
            return data

    def slices_redeem_slice_id_post_with_http_info(self, slice_id, **kwargs):  # noqa: E501
        """Redeem resources reserved via Create API  # noqa: E501

        Request that the reserved resources be made provisioned, instantiating or otherwise realizing the resources, such that they have a valid operational status and may possibly be made ready for experimenter use. This operation is synchronous, but may start a longer process, such as creating and imaging a virtual machine.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_redeem_slice_id_post_with_http_info(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_redeem_slice_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_redeem_slice_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/redeem/{sliceID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_renew_slice_id_post(self, slice_id, new_lease_end_time, **kwargs):  # noqa: E501
        """Renew slice  # noqa: E501

        Request to extend slice be renewed with their expiration extended. If possible, the orchestrator should extend the slivers to the requested expiration time, or to a sooner time if policy limits apply.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_renew_slice_id_post(slice_id, new_lease_end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :param str new_lease_end_time: New Lease End Time for the Slice (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_renew_slice_id_post_with_http_info(slice_id, new_lease_end_time, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_renew_slice_id_post_with_http_info(slice_id, new_lease_end_time, **kwargs)  # noqa: E501
            return data

    def slices_renew_slice_id_post_with_http_info(self, slice_id, new_lease_end_time, **kwargs):  # noqa: E501
        """Renew slice  # noqa: E501

        Request to extend slice be renewed with their expiration extended. If possible, the orchestrator should extend the slivers to the requested expiration time, or to a sooner time if policy limits apply.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_renew_slice_id_post_with_http_info(slice_id, new_lease_end_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :param str new_lease_end_time: New Lease End Time for the Slice (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slice_id', 'new_lease_end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_renew_slice_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_renew_slice_id_post`")  # noqa: E501
        # verify the required parameter 'new_lease_end_time' is set
        if ('new_lease_end_time' not in params or
                params['new_lease_end_time'] is None):
            raise ValueError("Missing the required parameter `new_lease_end_time` when calling `slices_renew_slice_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []
        if 'new_lease_end_time' in params:
            query_params.append(('newLeaseEndTime', params['new_lease_end_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/renew/{sliceID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_slice_id_get(self, slice_id, **kwargs):  # noqa: E501
        """slice properties  # noqa: E501

        Retrieve Slice properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_slice_id_get(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_slice_id_get_with_http_info(slice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_slice_id_get_with_http_info(slice_id, **kwargs)  # noqa: E501
            return data

    def slices_slice_id_get_with_http_info(self, slice_id, **kwargs):  # noqa: E501
        """slice properties  # noqa: E501

        Retrieve Slice properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_slice_id_get_with_http_info(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_slice_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_slice_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/{sliceID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def slices_status_slice_id_get(self, slice_id, **kwargs):  # noqa: E501
        """slice status  # noqa: E501

        Retrieve the status of a slice. Status would include dynamic reservation or instantiation information. This API is used to provide updates on the state of the resources after the completion of create, which began to asynchronously provision the resources. The response would contain relatively dynamic data, not descriptive data as returned in the Graph ML.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_status_slice_id_get(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.slices_status_slice_id_get_with_http_info(slice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.slices_status_slice_id_get_with_http_info(slice_id, **kwargs)  # noqa: E501
            return data

    def slices_status_slice_id_get_with_http_info(self, slice_id, **kwargs):  # noqa: E501
        """slice status  # noqa: E501

        Retrieve the status of a slice. Status would include dynamic reservation or instantiation information. This API is used to provide updates on the state of the resources after the completion of create, which began to asynchronously provision the resources. The response would contain relatively dynamic data, not descriptive data as returned in the Graph ML.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.slices_status_slice_id_get_with_http_info(slice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str slice_id: Slice identifier as UUID (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method slices_status_slice_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slice_id' is set
        if ('slice_id' not in params or
                params['slice_id'] is None):
            raise ValueError("Missing the required parameter `slice_id` when calling `slices_status_slice_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'slice_id' in params:
            path_params['sliceID'] = params['slice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/slices/status/{sliceID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
