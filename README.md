# Fabric Orchestrator swagger-client
This is Fabric Orchestrator API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Generating the Client Code
Due to a BUG in swagger-code-gen, Please follow the steps below

That said, there's a bug in the Python generator of Swagger Codegen 3.x, it doesn't generate the code for Bearer authentication in OpenAPI 3.0 definitions. 
As a workaround, edit your OpenAPI YAML file and replace this part

```
  securitySchemes:
    bearerAuth:     
      type: http
      scheme: bearer
      bearerFormat: JWT  
```

to

```
  securitySchemes:
    sso_auth:
      type: apiKey
      in: header
      name: Authorization
```
Then generate a new Python client from the modified API definition.


Reference for more details [here](https://stackoverflow.com/questions/57920052/how-to-set-the-bearer-token-in-the-python-api-client-generated-by-swagger-codege)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/fabric-testbed/OrchestratorClient.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/fabric-testbed/OrchestratorClient.git`)

Then import the package:
```python
import fabric.orchestrator.swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fabric.orchestrator.swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8700/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**version_get**](docs/DefaultApi.md#version_get) | **GET** /version | version
*ResourcesApi* | [**resources_get**](docs/ResourcesApi.md#resources_get) | **GET** /resources | Retrieve a listing and description of available resources
*SlicesApi* | [**slices_create_post**](docs/SlicesApi.md#slices_create_post) | **POST** /slices/create | Create slice
*SlicesApi* | [**slices_delete_slice_id_delete**](docs/SlicesApi.md#slices_delete_slice_id_delete) | **DELETE** /slices/delete/{sliceID} | Delete slice.
*SlicesApi* | [**slices_get**](docs/SlicesApi.md#slices_get) | **GET** /slices | Retrieve a listing of user slices
*SlicesApi* | [**slices_modify_slice_id_put**](docs/SlicesApi.md#slices_modify_slice_id_put) | **PUT** /slices/modify/{sliceID} | Modify slice
*SlicesApi* | [**slices_redeem_slice_id_post**](docs/SlicesApi.md#slices_redeem_slice_id_post) | **POST** /slices/redeem/{sliceID} | Redeem resources reserved via Create API
*SlicesApi* | [**slices_renew_slice_id_post**](docs/SlicesApi.md#slices_renew_slice_id_post) | **POST** /slices/renew/{sliceID} | Renew slice
*SlicesApi* | [**slices_slice_id_get**](docs/SlicesApi.md#slices_slice_id_get) | **GET** /slices/{sliceID} | slice properties
*SlicesApi* | [**slices_status_slice_id_get**](docs/SlicesApi.md#slices_status_slice_id_get) | **GET** /slices/status/{sliceID} | slice status
*SliversApi* | [**slivers_get**](docs/SliversApi.md#slivers_get) | **GET** /slivers | Retrieve a listing of user slivers
*SliversApi* | [**slivers_modify_sliver_id_put**](docs/SliversApi.md#slivers_modify_sliver_id_put) | **PUT** /slivers/modify/{sliverID} | Modify sliver
*SliversApi* | [**slivers_poa_sliver_id_post**](docs/SliversApi.md#slivers_poa_sliver_id_post) | **POST** /slivers/poa/{sliverID} | Perform Operational Action
*SliversApi* | [**slivers_sliver_id_get**](docs/SliversApi.md#slivers_sliver_id_get) | **GET** /slivers/{sliverID} | slivers properties
*SliversApi* | [**slivers_status_sliver_id_get**](docs/SliversApi.md#slivers_status_sliver_id_get) | **GET** /slivers/status/{sliverID} | slivers status

## Documentation For Models

 - [Success](docs/Success.md)
 - [Version](docs/Version.md)

## Documentation For Authorization


## bearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

kthare10@unc.edu
