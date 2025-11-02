# Creating a Company Vault

This example demonstrates how to create a company vault in Passwork using the Python connector.

## Use Case

You need to create a new company vault. Company vaults are shared vaults that can be accessed by multiple users within your organization.

## Basic Usage

Create a file `create_company_vault.py` with the following content:

```python
from passwork_client import PassworkClient
from passwork_client.exceptions import PassworkError

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

# Example: Create company vault
try:
    vault_name = "Company_vault"
    company_vault_type = passwork.find_vault_type(code="company")
    if not company_vault_type:
        raise PassworkError("Default 'company' vault type not found.")

    vault_id = passwork.create_vault(vault_name, company_vault_type["id"])
    print(f"Vault was created: {vault_id}")
except Exception as e:
    print(f"Error: {e}")
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating a company vault:

```shell
(api) passwork@api-integration:~# python3 create_company_vault.py 
Vault was created: 68d3c3e5473b357ee60a66bb
```

## How It Works

1. The script initializes the PassworkClient with your Passwork host address
2. It authenticates using the access token and refresh token
3. If client-side encryption is enabled, the master key is set
4. The script finds the default company vault type by its code
5. A new company vault is created with the specified name
6. The vault ID is returned and printed

## Important Notes

- **Access Token**: Required for authentication. Get it from the Passwork web interface
- **Refresh Token**: Optional but recommended for automatic token refresh
- **Master Key**: Required only if client-side encryption is enabled in your Passwork instance

