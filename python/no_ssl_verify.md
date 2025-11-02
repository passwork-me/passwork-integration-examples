# Disabling SSL Certificate Verification

This example demonstrates how to make requests to Passwork API with SSL certificate verification disabled using the Python connector.

## Use Case

You need to connect to Passwork when SSL certificate verification cannot be performed. This is useful for:
- Testing environments with self-signed certificates
- Development servers without proper SSL certificates
- Internal networks with custom certificate authorities
- Troubleshooting SSL-related connection issues

**Important**: Disabling SSL verification reduces security and makes connections vulnerable to man-in-the-middle attacks. **Only use this in development or trusted internal networks. Never use this in production.**

## Basic Usage

Create a file `no_ssl_verify.py` with the following content:

```python
import os
from passwork_client import PassworkClient

# Configuration
ACCESS_TOKEN = "FxWvuVqP9cPvAdWq3BMsSwVaEtFltaka49sv+2HjJME="
REFRESH_TOKEN = "2z7wR6gkNYSVBZEV3D/zddX+GW7LYuNN4WYOaZxHgMQ=" # Optional (required for token refresh)
MASTER_KEY = "EgOHwWQZcsgp/hFUAXS0PD60IUjxinfUEo8kUomhloumAXsRPtZ/7wTubtT7WXSpbfvKDDlm+yeOt5l5mN++IQ==" # Master key (if client-side encryption is enabled)
HOST = "https://passwork.example.org" # Passwork host address

# Initialize PassworkClient with SSL verification disabled
try:
    # Set verify_ssl=False to disable SSL certificate verification
    passwork = PassworkClient(HOST, verify_ssl=False)
    passwork.set_tokens(ACCESS_TOKEN, REFRESH_TOKEN)
    if bool(MASTER_KEY):
        passwork.set_master_key(MASTER_KEY)
except Exception as e:
    print(f"Login Error: {e}")
    exit(1)

# Example: Make API requests with SSL verification disabled
try:
    ITEM_ID = "68d3d19c3ea6febf700c740a"
    DOWNLOAD_PATH = os.path.join("./attachments", ITEM_ID)

    # Fetch the item
    item = passwork.get_item(ITEM_ID)
    
    # Uncomment the line below to download attachments for the item
    # passwork.download_item_attachment(item, DOWNLOAD_PATH)
    
    print(f"Decrypted item: {item}")
except Exception as e:
    print(f"Error getting item: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving an item:

```shell
(api) passwork@api-integration:~# python3 no_ssl_verify.py
{
    "id": "68d3d19c3ea6febf700c740a",
    "vaultId": "68d3c3b3473b357ee60a66b8",
    "folderId": null,
    "passwordEncrypted": "amt4cwv48xb6pp1h7564uuku8d44era25dn66ja39dhqcta4ddm6wy3m6dnpck36dgqm2f8",
    "keyEncrypted": "amt4cwv48xb6pp1h5xcqgcvr6gtq0xu3ehnk2v396993ayjt5wqpyxv1c586gtb8axk7mxvb84tm8thpd0rkcnk79hmn0nub9ntpyrv5b1n7jcu4c5r68x399xwnevupc8wpghbra5n7mhjp9x1n4cjgb9aqcnjhb566mm2u69ck0rucf5j4mjhf8t5myrbmctt4wp9ba5nkjmjc70qqmhubahu7acb48ha3crjj6t4pet3pf97ppx33b8w38rj7ehtqjxj2edupry3nb4yg",
    "customs": [],
    "attachments": [],
    "name": "Grafana Access",
    "login": "ldap_view_grafana@passwork.local",
    "url": "https://grafana.passwork.com",
    "description": "Item description",
    "tags": ["grafana", "monitoring"],
    "fieldsOrder": null,
    "isDeleted": false,
    "color": 0,
    "isFavorite": false,
    "password": "P@ssw0rd"
}
```

## How It Works

1. When initializing `PassworkClient`, set `verify_ssl=False` parameter to disable SSL certificate verification
2. All API requests made through this client instance will skip SSL certificate validation
3. The client authenticates using tokens and master key as usual
4. All standard operations (`get_item`, `create_item`, `update_item`, etc.) work normally, but without SSL verification

## Important Notes

- **Parameter Location**: Set `verify_ssl=False` when creating the `PassworkClient` instance: `PassworkClient(HOST, verify_ssl=False)`
- **Applies to All Requests**: Once set, SSL verification is disabled for all requests made through this client instance
- **Default Behavior**: By default, `PassworkClient` verifies SSL certificates (`verify_ssl=True`). Only set `verify_ssl=False` when absolutely necessary
- **Security Warning**: **Disabling SSL verification makes all connections vulnerable to man-in-the-middle attacks. Only use in development or trusted internal networks**
- **Production Usage**: **Never disable SSL verification in production environments** unless you have a specific security requirement
- **Self-Signed Certificates**: For development, consider installing self-signed certificates in your system's certificate store instead of disabling verification
- **Alternative Solutions**: If possible, use proper SSL certificates or configure your certificate authority (CA) instead of disabling verification

