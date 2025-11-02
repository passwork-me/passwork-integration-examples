# Creating a Private Vault

This example demonstrates how to create a private vault in Passwork using the Python connector.

## Use Case

You need to create a new private vault. Private vaults are personal vaults that belong to the user creating them and can be shared with other users if needed.

## Basic Usage

Create a file `create_private_vault.py` with the following content:

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

# Example: Create private vault
try:
    vault_name = "Python Private Vault"
    company_vault_type = passwork.find_vault_type(code="privateShared")
    vault_id = passwork.create_vault(vault_name, company_vault_type["id"])
    print(f"Vault was created: {vault_id}")
except Exception as e:
    print(f"Error: {e}")
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating a private vault:

```shell
(api) passwork@api-integration:~# python3 create_private_vault.py 
Vault was created: 68da51dde06b28a5df0d7752
```

## How It Works

1. The script initializes the PassworkClient with your Passwork host address
2. It authenticates using the access token and refresh token
3. If client-side encryption is enabled, the master key is set
4. The script finds the private vault type by its code (`privateShared`)
5. A new private vault is created with the specified name
6. The vault ID is returned and printed

## Important Notes

- **Access Token**: Required for authentication. Get it from the Passwork web interface
- **Refresh Token**: Optional but recommended for automatic token refresh
- **Master Key**: Required only if client-side encryption is enabled in your Passwork instance
- **Vault Type**: The script uses the `privateShared` vault type code
- **Private vs Company**: Private vaults belong to the user who creates them, while company vaults are shared organizational vaults