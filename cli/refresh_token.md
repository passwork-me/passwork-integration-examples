# Refreshing your access token

This example demonstrates how to refresh your Passwork API access token when it expires.

## Use case

Access tokens in Passwork have a limited lifetime. When they expire, you need to refresh them using your refresh token to obtain a new valid access token without having to log in again.

## Command

```bash
# Using the api command to refresh both access and refresh tokens
passwork-cli api \
  --host "https://passwork.example.com" \
  --token "your_expired_token" \
  --refresh-token "your_refresh_token" \
  --method POST \
  --endpoint "v1/sessions/refresh"
```

## Additional refresh endpoints

You can also call dedicated token refresh endpoints directly with `passwork-cli api`:

```bash
# Refresh only access token
passwork-cli api \
  --host "https://passwork.example.com" \
  --token "your_access_token" \
  --method POST \
  --endpoint "v1/sessions/refresh-access-token" \
  --params '{"accessToken":"your_access_token"}'

# Refresh only refresh token
passwork-cli api \
  --host "https://passwork.example.com" \
  --refresh-token "your_refresh_token" \
  --method POST \
  --endpoint "v1/sessions/refresh-refresh-token" \
  --params '{"refreshToken":"your_refresh_token"}'
```

## SSL parameters

For `api` commands, you can use the `--ssl-verify` parameter:

```bash
# Use system SSL verification explicitly
passwork-cli api --method GET --endpoint "v1/users/info" --ssl-verify

# Use a custom CA bundle/certificate directory
passwork-cli api --method GET --endpoint "v1/users/info" --ssl-verify "/etc/ssl/certs"
```

You can also use `--no-ssl-verify` if you need to disable SSL verification.

## How it works

1. Passwork CLI connects to your Passwork server
2. It sends a POST request to the refresh token endpoint
3. The server validates your refresh token
4. If valid, the server returns a new access token and refresh token as JSON

## Example response

The API returns a JSON response containing both the new access token and refresh token:

```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "refreshToken": "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.8sMVAOAiZUYJXGGQE_DvkEjgpaM1M-q0t8AjRqLSNAyKiKL3ykQni6GxCEzYRf0Y"
}
```

## Parsing the tokens in scripts

### Using jq (JSON processor)

If you have jq installed, it's easy to parse the JSON response:

```bash
#!/bin/bash

# Get the token response
RESPONSE=$(passwork-cli api \
  --host "https://passwork.example.com" \
  --token "your_expired_token" \
  --refresh-token "your_refresh_token" \
  --method POST \
  --endpoint "v1/sessions/refresh")

# Extract the tokens using jq
NEW_ACCESS_TOKEN=$(echo $RESPONSE | jq -r '.accessToken')
NEW_REFRESH_TOKEN=$(echo $RESPONSE | jq -r '.refreshToken')

```
