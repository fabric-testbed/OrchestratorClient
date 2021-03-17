# SliversApi

All URIs are relative to *http://127.0.0.1:8700/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slivers_get**](SliversApi.md#slivers_get) | **GET** /slivers | Retrieve a listing of user slivers
[**slivers_modify_sliver_id_put**](SliversApi.md#slivers_modify_sliver_id_put) | **PUT** /slivers/modify/{sliverID} | Modify sliver
[**slivers_poa_sliver_id_post**](SliversApi.md#slivers_poa_sliver_id_post) | **POST** /slivers/poa/{sliverID} | Perform Operational Action
[**slivers_sliver_id_get**](SliversApi.md#slivers_sliver_id_get) | **GET** /slivers/{sliverID} | slivers properties
[**slivers_status_sliver_id_get**](SliversApi.md#slivers_status_sliver_id_get) | **GET** /slivers/status/{sliverID} | slivers status

# **slivers_get**
> Success slivers_get(slice_id)

Retrieve a listing of user slivers

Retrieve a listing of user slivers

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SliversApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SliversApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID

try:
    # Retrieve a listing of user slivers
    api_response = api_instance.slivers_get(slice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SliversApi->slivers_get: %s\n" % e)
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

# **slivers_modify_sliver_id_put**
> Success slivers_modify_sliver_id_put(body, slice_id, sliver_id)

Modify sliver

Request to modify slice as described in the request. Request would be a Graph ML describing the requested resources for slice or a dictionary for sliver. On success, for one or more slivers are modified. This API returns list and description of the resources reserved for the slice in the form of Graph ML. Orchestrator would also trigger provisioning of the new resources on the appropriate sites either now or in the future based as requested. Modify operations may include add/delete/modify a container/VM/Baremetal server/network or other resources to the slice. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SliversApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SliversApi(ApiClient(configuration))
body = 'body_example' # str | 
slice_id = 'slice_id_example' # str | Slice identifier as UUID
sliver_id = 'sliver_id_example' # str | Sliver identifier as UUID

try:
    # Modify sliver
    api_response = api_instance.slivers_modify_sliver_id_put(body, slice_id, sliver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SliversApi->slivers_modify_sliver_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **slice_id** | **str**| Slice identifier as UUID | 
 **sliver_id** | **str**| Sliver identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slivers_poa_sliver_id_post**
> Success slivers_poa_sliver_id_post(body, sliver_id)

Perform Operational Action

Perform the named operational action on the named resources, possibly changing the operational status of the named resources. E.G. 'reboot' a VM.  

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SliversApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SliversApi(ApiClient(configuration))
body = 'body_example' # str | 
sliver_id = 'sliver_id_example' # str | Sliver identifier as UUID

try:
    # Perform Operational Action
    api_response = api_instance.slivers_poa_sliver_id_post(body, sliver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SliversApi->slivers_poa_sliver_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **sliver_id** | **str**| Sliver identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slivers_sliver_id_get**
> Success slivers_sliver_id_get(slice_id, sliver_id)

slivers properties

Retrieve Sliver properties

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SliversApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SliversApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID
sliver_id = 'sliver_id_example' # str | Sliver identifier as UUID

try:
    # slivers properties
    api_response = api_instance.slivers_sliver_id_get(slice_id, sliver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SliversApi->slivers_sliver_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 
 **sliver_id** | **str**| Sliver identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slivers_status_sliver_id_get**
> Success slivers_status_sliver_id_get(slice_id, sliver_id)

slivers status

Retrieve the status of a sliver. Status would include dynamic reservation or instantiation information. This API is used to provide updates on the state of the resources after the completion of create_slices, which began to asynchronously provision the resources. The response would contain relatively dynamic data, not descriptive data as returned in the Graph ML. 

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import SliversApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = SliversApi(ApiClient(configuration))
slice_id = 'slice_id_example' # str | Slice identifier as UUID
sliver_id = 'sliver_id_example' # str | Sliver identifier as UUID

try:
    # slivers status
    api_response = api_instance.slivers_status_sliver_id_get(slice_id, sliver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SliversApi->slivers_status_sliver_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slice_id** | **str**| Slice identifier as UUID | 
 **sliver_id** | **str**| Sliver identifier as UUID | 

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

