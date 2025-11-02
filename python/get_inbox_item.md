# Getting an Inbox Item

This example demonstrates how to retrieve and decrypt an item from the inbox in Passwork using the Python connector.

## Use Case

You need to retrieve an item that was shared with you through the Passwork inbox. Inbox items are password entries that have been shared with you by other users, and they are automatically decrypted using your master key.

## Basic Usage

Create a file `get_inbox_item.py` with the following content:

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

# Example: Get inbox item
try:
    INBOX_ID = "68da5bfef28bf56cec08c534"
    inbox = passwork.get_inbox_item(INBOX_ID)
    download_path = os.path.join("./attachments", INBOX_ID)
    
    # If you need to download an attachment from the item
    #passwork.download_inbox_attachment(inbox, download_path)

    print(f"Decrypted inbox password: {inbox}") 

except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving an inbox item:

```shell
(api) passwork@api-integration:~# python3 get_inbox_item.py
{
    "id": "68d3d19c3ea6febf700c740a",
    "vaultId": "68d3c3b3473b357ee60a66b8",
    "folderId": null,
    "passwordEncrypted": "amt4cwv48xb6pp1h71948k1qf5ppcpa1f8un0ya4dtp54hv69ngmgmhg9x86guvf5xj3ed32d1vn6j9rd53pekj49h4pgthh89h66ur",
    "keyEncrypted": "amt4cwv48xb6pp1h5xcqgcvr6gtq0xu3ehnk2v396993ayjt5wqpyxv1c586gtb8axk7mxvb84tm8thpd0rkcnk79hmn0nub9ntpyrv5b1n7jcu4c5r68x399xwnevupc8wpghbra5n7mhjp9x1n4cjgb9aqcnjhb566mm2u69ck0rucf5j4mjhf8t5myrbmctt4wp9ba5nkjmjc70qqmhubahu7acb48ha3crjj6t4pet3pf97ppx33b8w38rj7ehtqjxj2edupry3nb4yg",
    "customs": [],
    "attachments": [],
    "name": "Grafana Access",
    "login": "ldap_view_grafana@passwork.local",
    "url": "https://grafana.passwork.com",
    "description": "Access with Grafana configuration capability",
    "tags": [
        "grafana"
    ],
    "fieldsOrder": null,
    "isDeleted": false,
    "color": 0,
    "isFavorite": false,
    "inbox": {
        "id": "68da5bfef28bf56cec08c534",
        "keyEncrypted": "AHF8fgB2yGz44wSkaX7OKVcKghyN+Kfo/uZx+aGaoXuBupch9c9CRvP7UNqc5AfHakkV5INeNtRfhYGUkai1CM0RCScPVutJwsdiQxG0irkX82NsaZnSfxuK5G+HcxG9kbypundzzJbW2V28gBqsE7wX3JWGZwIOL/mhwJisfbgxRDYjj/tiLrMnSCUYITFoAnpUBP0KE2jcxV25W5KZVlKO9SoCP0gnqujEbZvbaNYl8uTSJvUKqfRYeoibUOK7YNu0QgcnDpqOhrGVFHYFT824tdwdtGCEHHHDNzJE5xL7I4CJjfYSKH9NZM5NkjwfwCZ3wNEoHPybEcSr0DNAPg==",
        "access": "write",
        "senderId": "687a8f1fa2798e2f89032553",
        "createdAt": 1759140862,
        "isViewed": true,
        "isUserNotified": true,
        "sender": {
            "id": "687a8f1fa2798e2f89032553",
            "login": "ldap_mid_10",
            "fullName": "ldap_mid_10",
            "hasAvatar": false,
            "isDeleted": false
        }
    },
    "password": "fxS9:y3zwUEP=RB0Ca-M"
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `INBOX_ID` of the inbox item to retrieve
3. The `get_inbox_item()` method retrieves and automatically decrypts the inbox item
4. The item is decrypted using your master key, so you can access all fields including the password
5. Optionally, you can download attachments from the inbox item using `download_inbox_attachment()`
6. The decrypted item data is returned with all fields visible, including inbox metadata (sender, access level, etc.)

## Important Notes

- **Inbox ID**: Required. The ID of the inbox item you want to retrieve. You can find inbox IDs in your Passwork inbox
- **Master Key**: Required. The item is automatically decrypted using your master key if client-side encryption is enabled
- **Attachments**: If the inbox item has attachments, you can download them using `download_inbox_attachment()`. Uncomment that line and provide a download path
- **Inbox Metadata**: The response includes inbox-specific information such as sender details, access level, and view status
- **Decryption**: Inbox items are automatically decrypted by the connector using your master key
- **Access Level**: The inbox metadata shows the access level granted (read or read and write)
- **Sender Information**: The response includes information about who shared the item with you

