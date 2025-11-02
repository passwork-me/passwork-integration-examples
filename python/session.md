# Authentication and Token Management

This example demonstrates authentication and token management in Passwork using the Python connector, including automatic token rotation, session saving, and loading.

## Authentication and Token Handling

The Python connector supports working with tokens:

- Ability to save and reuse previously set tokens
- Automatic token refresh when `ACCESS_TOKEN` expires (if `REFRESH_TOKEN` is provided)

## Automatic Token Rotation

To enable automatic token rotation, specify the `auto_refresh=True` parameter when creating a `PassworkClient` instance. In this mode, if the API returns an `accessTokenExpired` error, the connector automatically calls token refresh and retries the request without manual intervention.

### update_tokens

The function updates `accessToken` using a previously issued `refreshToken`. It doesn't accept arguments and works with the current state of the `PassworkClient` instance.

Actions performed:
- Rotates `accessToken` and `refreshToken` via API request
- Updates corresponding fields in the client instance
- If tokens were saved to a file (via `save_session`), automatically updates the saved values

We recommend using automatic token rotation together with saving tokens (and master key) to a separate file.

## Saving and Loading Tokens

The Python connector supports saving received tokens (and master key) to a separate file. Data can be loaded from environment variables or directly from automation scripts. When saving, encryption is performed using a randomly generated key.

For working with saving and loading tokens, the following functions are provided:
- `save_session`
- `load_session`

### save_session

The function is designed to save tokens and (optionally) master key from a `PassworkClient` instance.

Parameters:
- `file_path` — path and filename where encrypted data will be stored. Example: `"/opt/access/api_passwork_tokens"`
- `encryption_key` — encryption key:
  - On first use, it's recommended to pass `None` — the connector will automatically generate a key and encrypt the data
  - On subsequent calls, you must pass the previously generated key
- `save_master_key` — flag determining whether to save and encrypt the user's master key in the file together with tokens

### load_session

The function is designed to load saved tokens and (optionally) master key from an encrypted file.

Parameters:
- `file_path` — path and filename from which encrypted data will be loaded
- `encryption_key` — encryption key that was used when saving tokens and (optionally) master key

## Basic Example

Initially, tokens and master key are located in environment variables and will be retrieved from there into a .py script to create a private vault.

Import tokens and (optionally) master key:

```shell
export PASSWORK_TOKEN="AyyR+yWe27xoPMd3502YmcyLR7j/+8dZnXYFvdn+w1o="
export PASSWORK_REFRESH_TOKEN="cF1krXop6sUoDrbGTt0dNRtOrvCG3uK98/vtVCjZRJY="
export PASSWORK_MASTER_KEY="EgOHwWQZcsgp/hFUAXS0PD60IUjxinfUEo8kUomhloumAXsRPtZ/7wTubtT7WXSpbfvKDDlm+yeOt5l5mN++IQ=="
```

Create a file `create_vault.py` and place the following:

```python
import os
from passwork_client import PassworkClient
from passwork_client.exceptions import PassworkError

passwork = PassworkClient(host="https://passwork.example.org", verify_ssl=True, auto_refresh=True) # Or PassworkClient(host="https://passwork.example.com", True, True)
passwork.set_tokens(os.getenv("PASSWORK_TOKEN"), os.getenv("PASSWORK_REFRESH_TOKEN"))
passwork.set_master_key(os.getenv("PASSWORK_MASTER_KEY"))

# Load tokens from encrypted file
# passwork.load_session("/opt/access/api_passwork_tokens", "encryption_key")
# Comment out on first automation run as encrypted file hasn't been created yet

vault_name = "DevOps"
company_vault_type = passwork.find_vault_type(name="DevOps")
vault_id = passwork.create_vault(vault_name, company_vault_type["id"])
print(f"Vault was created: {vault_id}")

# Save tokens to encrypted file
encryption_key = passwork.save_session("/opt/access/api_passwork_tokens", encryption_key=None, save_master_key=True) # Or passwork.save_session("path", None, True)
# Do not specify a value in encryption_key, encryption key will be generated

# Get randomly generated encryption key
print(f"Encryption key: {encryption_key}")
```

Save the file and run:

```shell
python3 create_vault.py
```

Example of correct output:

```shell
Encryption key: bjteL538FXzL2GSIO7qCTt5kOujpYrBVX9bCgzdnC+A=
Vault was created: 68dbc69a6e6ccb8154015b72
```

Edit the `create_vault.py` script:
- Comment out/Delete passing tokens and (optionally) master key
- Uncomment loading tokens and (optionally) master key from encrypted file using encryption key

```python
import os
from passwork_client import PassworkClient
from passwork_client.exceptions import PassworkError

passwork = PassworkClient("https://passwork.example.com", True, True)

# Load tokens from encrypted file
passwork.load_session("/opt/access/api_passwork_tokens", "bjteL538FXzL2GSIO7qCTt5kOujpYrBVX9bCgzdnC+A=")
# Comment out on first automation run as encrypted file hasn't been created yet

vault_name = "DevOps"
company_vault_type = passwork.find_vault_type(name="DevOps")
vault_id = passwork.create_vault(vault_name, company_vault_type["id"])
print(f"Vault was created: {vault_id}")

# Save tokens to encrypted file
passwork.save_session("/opt/access/api_passwork_tokens", "bjteL538FXzL2GSIO7qCTt5kOujpYrBVX9bCgzdnC+A=", True)
# Do not specify a value in encryption_key, encryption key will be generated
```

To avoid storing the encryption key for decrypting tokens in a file, you can pass it to the Python script in one of the following ways:

- **Environment Variables (ENV)** — set the key via environment and subsequently read it using `os.environ`
- **Command Line Arguments (argparse)** — pass the key when running the script with argument parsing
- **Standard Input (STDIN, pipe, or here-doc)** — the key is read from input stream without appearing in the process argument list
- **Interactive Input (getpass)** — secure prompt for the key from the user at runtime (characters are not displayed on screen)

## Important Notes

- **Automatic Token Rotation**: When `auto_refresh=True` is set, expired tokens are automatically refreshed without manual intervention
- **Encryption Key**: On first save, always pass `None` to let the connector generate a secure random key
- **Security**: Store the encryption key securely. Do not commit it to version control or expose it in logs
- **Master Key**: Setting `save_master_key=True` saves the master key along with tokens, enabling full client functionality after loading
- **Token Updates**: When using automatic refresh, tokens saved in files are automatically updated after refresh
- **File Path**: Use absolute paths for session files to avoid path resolution issues
- **First Run**: On the first run, comment out `load_session` as the encrypted file doesn't exist yet

