# Getting an Item

This example demonstrates how to retrieve and decrypt an item from Passwork using the Python connector.

## Use Case

You need to retrieve an item by its ID and access its decrypted data. Items are automatically decrypted using your master key, allowing you to access all fields including passwords, custom fields, and metadata.

## Basic Usage

Create a file `get_item.py` with the following content:

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

# Example: Get item
try:
    ITEM_ID = "68d8377954f0c66ba70cf40b"
    DOWNLOAD_PATH = os.path.join("./attachments", ITEM_ID)

    item = passwork.get_item(ITEM_ID)

    # If you need to download an attachment from the item
    #passwork.download_item_attachment(item, DOWNLOAD_PATH)
    print(f"Decrypted item: {item}")
except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving an item:

```shell
(api) passwork@api-integration:~# python3 get_item.py
{
    "id": "68d8377954f0c66ba70cf40b",
    "vaultId": "68d835957229742928084234",
    "folderId": null,
    "passwordEncrypted": "amt4cwv48xb6pp1h5dpmgj3kchbncxvk8ntkeeaja5tnjkuq69r2pt2961d4guk99ngmgpk2a5d78d9ne1770p38ex7m6d2uen7mgu0",
    "keyEncrypted": "amt4cwv48xb6pp1h7542ynktd94p6ebcb94m4chbcx8n4t3b8rqp4nhj95nkak23dxv6uh2h65p5eg9q8t8k2g9md4t34paq8xv5gt9m89hk6j9ncdc42gbccn4mwhbma193jtueb5cmjw9pemwk4gkuenjqgkbrf9umjdk7ddup4w1b9hn32v37cdcqjea665bm2ebpdtrpjvbca4rmmmthe11k8p3ge9c70kvc9duprdkud8v4eckucxwpyx3fd8un2cad5xd4pj2k9myg",
    "customs": [],
    "attachments": [],
    "name": "PostgreSQL User",
    "login": "pguser_login",
    "url": "192.168.1.124:5433",
    "description": null,
    "tags": [
        "postgresql"
    ],
    "fieldsOrder": null,
    "isDeleted": false,
    "color": 0,
    "isFavorite": false,
    "vaultMasterKeyEncrypted": "UvwsZHx63UbQvDLeGkN/MnkOi3F4TMMAPuK9oRchanIP+nPiQTgCOwTsdvclGrvc6QKbVWgu0bFoEyEvSQVBWwtF+Seh5N0BniL19D6AWrglJPz9/s8w1tpaSwsN4fWttpLpiH9OEsJI8OqhcylnLsD3JitFjHPIl78vd8Y+nSzrmyzLTN6SsWKuwD5Q50hXLswXthsJEm83xEld9ZlmU85adm0oxlDGgYUJxBrljKg8s3LuAtiwKGd7r+Rz7F3RPNqEAKyrNFONRwGr9UIH2SKcLZ6ks3G5VZDGtmJO+tdKex4ROuY0O2zDva5BY5H4GHkJf2WHZ3XA6Zrxh8tLZw==",
    "password": "4a[Gn38tL)m[-))KSr8c"
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `ITEM_ID` of the item to retrieve
3. The `get_item()` method retrieves the item from Passwork
4. The item is automatically decrypted using your master key
5. All fields become accessible, including the password, custom fields, and metadata
6. Optionally, you can download attachments from the item using `download_item_attachment()`

## Important Notes

- **Item ID**: Required. Get it from the item URL in the Passwork web interface
- **Master Key**: Required if client-side encryption is enabled. The item will be automatically decrypted using your master key
- **Attachments**: If the item has attachments, you can download them using `download_item_attachment()`. Uncomment the relevant line and provide a download path
- **Decryption**: Items are automatically decrypted by the connector, so you can access all fields including passwords
- **Permissions**: Ensure you have permission to access the item and the vault it belongs to
- **Response Format**: The response includes all item fields, metadata (vault ID, folder ID, tags), and decrypted values