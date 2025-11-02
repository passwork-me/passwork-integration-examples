# Making Direct API Calls

This example demonstrates how to make direct API calls to Passwork using the Python connector's `call()` method.

## Use Case

You need to perform API operations that are not covered by the standard methods of the PassworkClient. The `call()` method allows you to make direct HTTP requests to any Passwork API endpoint.

## Basic Usage

Create a file `general_call.py` with the following content:

```python
from passwork_client import PassworkClient

# Configuration
ACCESS_TOKEN = "FxWvuVqP9cPvAdWq3BMsSwVaEtFltaka49sv+2HjJME="
REFRESH_TOKEN = "2z7wR6gkNYSVBZEV3D/zddX+GW7LYuNN4WYOaZxHgMQ=" # Optional (required for token refresh)
MASTER_KEY = "EgOHwWQZcsgp/hFUAXS0PD60IUjxinfUEo8kUomhloumAXsRPtZ/7wTubtT7WXSpbfvKDDlm+yeOt5l5mN++IQ==" # Master key (if client-side encryption is enabled)
HOST = "https://passwork.example.org" # Passwork host address

# Login to Passwork
try:
    passwork = PassworkClient(HOST)
    passwork.set_tokens(ACCESS_TOKEN, REFRESH_TOKEN)
    if bool(MASTER_KEY):
        passwork.set_master_key(MASTER_KEY)
except Exception as e:
    print(f"Error: {e}") 
    exit(1)

# Example: Direct API call
try:
    # Example: Delete folder
    FOLDER_ID = "687f92089ded1276bb053f66" 
   
    response = passwork.call("DELETE", f"/api/v1/folders/{FOLDER_ID}")
    print(f"Response: {response}") 

except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully executing the request:

```shell
(api) passwork@api-integration:~# python3 general_call.py 
Response: {'binItemId': '68da59afbf68ddc3b80d2346'}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. The `call()` method is used to make a direct HTTP request to the Passwork API
3. The method accepts an HTTP method (GET, POST, PUT, DELETE, etc.) and an API endpoint path
4. Optionally, you can pass query parameters or request body data as a third parameter
5. The API response is returned and can be processed as needed

## Important Notes

- **HTTP Methods**: Supported methods include GET, POST, PUT, DELETE, PATCH
- **API Endpoints**: Use the full API endpoint path, e.g., `/api/v1/folders/{FOLDER_ID}`
- **Query Parameters**: Pass query parameters as a dictionary in the third parameter: `passwork.call("GET", "/api/v1/endpoint", {"param1": "value1"})`
- **Request Body**: For POST/PUT requests, pass the body data as a dictionary in the third parameter
- **Authentication**: The access token is automatically included in the request headers
- **API Documentation**: Refer to the Passwork API documentation (Api reference.pdf) for available endpoints and parameters
- **Error Handling**: API errors will raise exceptions that should be caught and handled appropriately

