# ResourcesApi

All URIs are relative to *http://127.0.0.1:8700/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_get**](ResourcesApi.md#resources_get) | **GET** /resources | Retrieve a listing and description of available resources

# **resources_get**
> Success resources_get(level)

Retrieve a listing and description of available resources

Retrieve a listing and description of available resources

### Example
```python
from __future__ import print_function
import time
from fabric_cf.orchestrator.swagger_client import ResourcesApi, Configuration, ApiClient
from fabric_cf.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ResourcesApi(ApiClient(configuration))
level = 1 # int | Level of details (default to 1)

try:
    # Retrieve a listing and description of available resources
    api_response = api_instance.resources_get(level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **int**| Level of details | [default to 1]

### Return type

[**Success**](Success.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

