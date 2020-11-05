# swagger_client.DefaultApi

All URIs are relative to *http://127.0.0.1:8700/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get**](DefaultApi.md#version_get) | **GET** /version | version

# **version_get**
> Version version_get()

version

Version

### Example
```python
from __future__ import print_function
import time
import fabric.orchestrator.swagger_client
from fabric.orchestrator.swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = fabric.orchestrator.swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = fabric.orchestrator.swagger_client.DefaultApi(fabric.orchestrator.swagger_client.ApiClient(configuration))

try:
    # version
    api_response = api_instance.version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

