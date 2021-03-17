# SlicesApi

All URIs are relative to *http://127.0.0.1:8700/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slices_create_post**](SlicesApi.md#slices_create_post) | **POST** /slices/create_slices | Create slice
[**slices_delete_slice_id_delete**](SlicesApi.md#slices_delete_slice_id_delete) | **DELETE** /slices/delete/{sliceID} | Delete slice.
[**slices_get**](SlicesApi.md#slices_get) | **GET** /slices | Retrieve a listing of user slices
[**slices_modify_slice_id_put**](SlicesApi.md#slices_modify_slice_id_put) | **PUT** /slices/modify/{sliceID} | Modify slice
[**slices_redeem_slice_id_post**](SlicesApi.md#slices_redeem_slice_id_post) | **POST** /slices/redeem/{sliceID} | Redeem resources reserved via Create API
[**slices_renew_slice_id_post**](SlicesApi.md#slices_renew_slice_id_post) | **POST** /slices/renew/{sliceID} | Renew slice
[**slices_slice_id_get**](SlicesApi.md#slices_slice_id_get) | **GET** /slices/{sliceID} | slice properties
[**slices_status_slice_id_get**](SlicesApi.md#slices_status_slice_id_get) | **GET** /slices/status/{sliceID} | slice status

# **slices_create_post**
> Success slices_create_post(body, slice_name)

Create slice

Request to create_slices slice as described in the request. Request would be a graph ML describing the requested resources. Resources may be requested to be created now or in future. On success, one or more slivers are allocated, containing resources satisfying the request, and assigned to the given slice. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of these resources asynchronously on the appropriate sites either now or in the future as requested. Experimenter can invoke get slice API to get the latest state of the requested resources.  

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
body = 'body_example' # str | 
slice_name = 'slice_name_example' # str | Slice Name
ssh_key = 'ssh_key_example' # str | User SSH Key

try:
    # Create slice
    api_response = api_instance.slices_create_post(body, slice_name, ssh_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **slice_name** | **str**| Slice Name | 
 **ssh_key** | **str**| User SSH Key | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_delete_slice_id_delete**
> Success slices_delete_slice_id_delete(slice_id)

Delete slice.

Request to delete slice. On success, resources associated with slice or sliver are stopped if necessary, de-provisioned and un-allocated at the respective sites. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # Delete slice.
    api_response = api_instance.slices_delete_slice_id_delete(slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_delete_slice_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_get**
> Success slices_get()

Retrieve a listing of user slices

Retrieve a listing of user slices

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))

try:
    # Retrieve a listing of user slices
    api_response = api_instance.slices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_modify_slice_id_put**
> Success slices_modify_slice_id_put(body, slice_id)

Modify slice

Request to modify slice as described in the request. Request would be a Graph ML describing the requested resources for slice or a dictionary for sliver. On success, for one or more slivers are modified. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of the new resources on the appropriate sites either now or in the future based as requested. Modify operations may include add/delete/modify a container/VM/Baremetal server/network or other resources to the slice. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
body = 'body_example' # str | 
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # Modify slice
    api_response = api_instance.slices_modify_slice_id_put(body, slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_modify_slice_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **slice_id** | **str**| Slice identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_redeem_slice_id_post**
> Success slices_redeem_slice_id_post(slice_id)

Redeem resources reserved via Create API

Request that the reserved resources be made provisioned, instantiating or otherwise realizing the resources, such that they have a valid operational status and may possibly be made ready for experimenter use. This operation is synchronous, but may start a longer process, such as creating and imaging a virtual machine. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # Redeem resources reserved via Create API
    api_response = api_instance.slices_redeem_slice_id_post(slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_redeem_slice_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_renew_slice_id_post**
> Success slices_renew_slice_id_post(slice_id, new_lease_end_time)

Renew slice

Request to extend slice be renewed with their expiration extended. If possible, the orchestrator should extend the slivers to the requested expiration time, or to a sooner time if policy limits apply. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID
new_lease_end_time = 'new_lease_end_time_example' # str | New Lease End Time for the Slice

try:
    # Renew slice
    api_response = api_instance.slices_renew_slice_id_post(slice_id, new_lease_end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_renew_slice_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 
 **new_lease_end_time** | **str**| New Lease End Time for the Slice | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_slice_id_get**
> Success slices_slice_id_get(slice_id)

slice properties

Retrieve Slice properties

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # slice properties
    api_response = api_instance.slices_slice_id_get(slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_slice_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slices_status_slice_id_get**
> Success slices_status_slice_id_get(slice_id)

slice status

Retrieve the status of a slice. Status would include dynamic reservation or instantiation information. This API is used to provide updates on the state of the resources after the completion of create_slices, which began to asynchronously provision the resources. The response would contain relatively dynamic data, not descriptive data as returned in the Graph ML. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SlicesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SlicesApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # slice status
    api_response = api_instance.slices_status_slice_id_get(slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlicesApi->slices_status_slice_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

