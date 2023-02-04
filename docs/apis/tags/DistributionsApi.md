<a name="__pageTop"></a>
# python_opendota.apis.tags.distributions_api.DistributionsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_get**](#distributions_get) | **get** /distributions | GET /distributions

# **distributions_get**
<a name="distributions_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} distributions_get()

GET /distributions

Distributions of MMR data by bracket and country

### Example

```python
import python_opendota
from python_opendota.apis.tags import distributions_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = distributions_api.DistributionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /distributions
        api_response = api_instance.distributions_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling DistributionsApi->distributions_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#distributions_get.ApiResponseFor200) | Success

#### distributions_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[ranks](#ranks)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | ranks | [optional] 
**[mmr](#mmr)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | mmr | [optional] 
**[country_mmr](#country_mmr)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | country_mmr | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ranks

ranks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ranks | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commmand** | str,  | str,  | command | [optional] 
**rowCount** | decimal.Decimal, int,  | decimal.Decimal,  | rowCount | [optional] 
**[rows](#rows)** | list, tuple,  | tuple,  | rows | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  | fields | [optional] 
**rowAsArray** | bool,  | BoolClass,  | rowAsArray | [optional] 
**[sum](#sum)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rows

rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | rows | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bin** | decimal.Decimal, int,  | decimal.Decimal,  | bin | [optional] 
**bin_name** | decimal.Decimal, int,  | decimal.Decimal,  | bin_name | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | count | [optional] 
**cumulative_sum** | decimal.Decimal, int,  | decimal.Decimal,  | cumulative_sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | fields | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | name | [optional] 
**tableID** | decimal.Decimal, int,  | decimal.Decimal,  | tableID | [optional] 
**columnID** | decimal.Decimal, int,  | decimal.Decimal,  | columnID | [optional] 
**dataTypeID** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeID | [optional] 
**dataTypeSize** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeSize | [optional] 
**dataTypeModifier** | str,  | str,  | dataTypeModifier | [optional] 
**format** | str,  | str,  | format | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sum

sum

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | sum | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | count | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mmr

mmr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | mmr | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commmand** | str,  | str,  | command | [optional] 
**rowCount** | decimal.Decimal, int,  | decimal.Decimal,  | rowCount | [optional] 
**[rows](#rows)** | list, tuple,  | tuple,  | rows | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  | fields | [optional] 
**rowAsArray** | bool,  | BoolClass,  | rowAsArray | [optional] 
**[sum](#sum)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rows

rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | rows | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bin** | decimal.Decimal, int,  | decimal.Decimal,  | bin | [optional] 
**bin_name** | decimal.Decimal, int,  | decimal.Decimal,  | bin_name | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | count | [optional] 
**cumulative_sum** | decimal.Decimal, int,  | decimal.Decimal,  | cumulative_sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | fields | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | name | [optional] 
**tableID** | decimal.Decimal, int,  | decimal.Decimal,  | tableID | [optional] 
**columnID** | decimal.Decimal, int,  | decimal.Decimal,  | columnID | [optional] 
**dataTypeID** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeID | [optional] 
**dataTypeSize** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeSize | [optional] 
**dataTypeModifier** | str,  | str,  | dataTypeModifier | [optional] 
**format** | str,  | str,  | format | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sum

sum

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | sum | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | count | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# country_mmr

country_mmr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | country_mmr | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commmand** | str,  | str,  | command | [optional] 
**rowCount** | decimal.Decimal, int,  | decimal.Decimal,  | rowCount | [optional] 
**[rows](#rows)** | list, tuple,  | tuple,  | rows | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  | fields | [optional] 
**rowAsArray** | bool,  | BoolClass,  | rowAsArray | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rows

rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | rows | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**loccountrycode** | str,  | str,  | loccountrycode | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | count | [optional] 
**avg** | str,  | str,  | avg | [optional] 
**common** | str,  | str,  | common | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | fields | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | name | [optional] 
**tableID** | decimal.Decimal, int,  | decimal.Decimal,  | tableID | [optional] 
**columnID** | decimal.Decimal, int,  | decimal.Decimal,  | columnID | [optional] 
**dataTypeID** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeID | [optional] 
**dataTypeSize** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeSize | [optional] 
**dataTypeModifier** | decimal.Decimal, int,  | decimal.Decimal,  | dataTypeModifier | [optional] 
**format** | str,  | str,  | format | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

