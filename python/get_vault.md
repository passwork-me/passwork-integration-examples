# Getting a Vault

This example demonstrates how to retrieve vault information in Passwork using the Python connector.

## Use Case

You need to retrieve detailed information about a vault, including its name, type, permissions, and access settings. This is useful for checking vault properties, permissions, and configuration.

## Basic Usage

Create a file `get_vault.py` with the following content:

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

# Example: Get vault
try:
    VAULT_ID = "687663896eea6641b6065cd8" 
    vault = passwork.get_vault(VAULT_ID) 
    print(f"Vault: {vault}") 
except Exception as e:
    print(f"Error: {e}")
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving vault information:

```shell
(api) passwork@api-integration:~# python3 get_vault.py
{
    "id": "687663896eea6641b6065cd8",
    "name": "api_vaults_01",
    "typeId": "685cfa5a3d0ba75d2f041972",
    "permissions": [
        "directory:read",
        "directory:edit",
        "directory:copy",
        "directory:move",
        "directory:delete",
        "directory:export",
        "directory:activityLog:read",
        "directory:security:analyse",
        "directory:access:read",
        "directory:access:manage",
        "vault:delete",
        "object:createAndImport",
        "item:read",
        "item:edit",
        "item:delete",
        "item:move",
        "item:copy",
        "item:snapshot:read",
        "item:activityLog:read",
        "shortcut:create",
        "inboxItem:createForReading",
        "inboxItem:createForEditing",
        "link:create",
        "item:additionalAccess:read",
        "item:additionalAccess:manage",
        "bin:manage",
        "vault:leave"
    ],
    "masterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
    "isVisible": true,
    "directoryAccess": {
        "isViewingAccess": false,
        "access": "admin",
        "accessName": "Administration"
    },
    "canLeaveVault": null,
    "canChangeVaultType": null
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `VAULT_ID` of the vault to retrieve
3. The `get_vault()` method retrieves detailed vault information
4. The response includes vault metadata, permissions, access settings, and configuration
5. The encrypted master key is included if client-side encryption is enabled

## Important Notes

- **Vault ID**: Required. Get it from the vault URL in the Passwork web interface (e.g., `https://passwork.example.org/VAULT_ID`)
- **Vault Information**: The response includes vault name, type ID, visibility status, and permissions
- **Permissions**: The `permissions` array lists all permissions you have for this vault, including item operations, directory management, and vault administration
- **Access Level**: The `directoryAccess` field shows your access level
- **Master Key**: If client-side encryption is enabled, the `masterKeyEncrypted` field contains the encrypted vault master key
- **Vault Type**: The `typeId` field identifies the type of vault (company, private, etc.)
- **Visibility**: The `isVisible` field indicates whether the vault is visible in your interface
- **Permissions**: Ensure you have at least read permission to access the vault information