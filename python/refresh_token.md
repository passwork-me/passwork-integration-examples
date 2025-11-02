# Refreshing Tokens

This example demonstrates how to refresh tokens in Passwork using the Python connector.

## Use Case

You need to refresh your access token to maintain authentication. Access tokens expire after a certain period, and refreshing them extends your session without requiring user interaction.

## Basic Usage

Create a file `refresh_token.py` with the following content:

```python
from passwork_client import PassworkClient
import os

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

# Example: Refresh tokens
try:
    tokens = passwork.update_tokens()
    print(f"Tokens: {tokens}")
except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully refreshing tokens:

```shell
(api) passwork@api-integration:~# python3 refresh_token.py 
Tokens: {'accessToken': '5g92HR0yJ4m51NIIy4djM9ozd44Juftg/og+KzyoLy8=', 'refreshToken': 'JCTrsUqz+3P/1xK4bGRM9JTjDmL+kqtlzsau7REJads=', 'accessTokenExpiredAt': 1759753535}
```

## How It Works

1. The script initializes the PassworkClient with your current access token and refresh token
2. It calls the `update_tokens()` method, which uses the refresh token to obtain new tokens
3. The method returns a dictionary containing:
   - `accessToken`: The new access token
   - `refreshToken`: The new refresh token
   - `accessTokenExpiredAt`: Unix timestamp indicating when the new access token expires
4. The new tokens should be saved and used for subsequent API calls

## Important Notes

- **Refresh Token**: Required. The refresh token must be valid and not expired
- **Token Expiration**: Access tokens expire after a certain period. Refresh tokens allow you to obtain new access tokens without re-authenticating
- **Save New Tokens**: After refreshing, save the new tokens and use them for subsequent requests
- **Automatic Refresh**: Some implementations can automatically refresh tokens when they expire, but this example shows manual refresh
- **Token Lifetime**: The `accessTokenExpiredAt` field indicates when the new access token will expire
- **Security**: Keep tokens secure and do not expose them in logs or version control
- **Token Updates**: After refreshing, update your stored tokens (in environment variables, configuration files, etc.) for future use