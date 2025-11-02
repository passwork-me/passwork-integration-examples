# Getting a Shortcut

This example demonstrates how to retrieve and decrypt a shortcut in Passwork using the Python connector.

## Use Case

You need to retrieve a shortcut by its ID and access its data. Shortcuts are references to items that can be placed in different vaults or folders. When you retrieve a shortcut, you get both the shortcut information and the original item data.

## Basic Usage

Create a file `get_shortcut.py` with the following content:

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

# Example: Get shortcut
try:
    SHORTCUT_ID = "68d6c94bec3a3fe41209546e"
    # If you need to download an attachment from the shortcut
    #DOWNLOAD_PATH = os.path.join("./attachments", SHORTCUT_ID) 

    shortcut = passwork.get_shortcut(SHORTCUT_ID) 
    
    # If you need to download an attachment from the shortcut
    #passwork.download_shortcut_attachment(shortcut, DOWNLOAD_PATH)
    
    print(f"Decrypted shortcut: {shortcut}") 

except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving a shortcut:

```shell
(api) passwork@api-integration:~# python3 get_shortcut.py
{
    "id": "68793e13dfc88d879e0f2e39",
    "vaultId": "687663896eea6641b6065cd8",
    "folderId": null,
    "passwordEncrypted": "amt4cwv48xb6pp1h75wqacjha1kn0p328dn32tuuetrpuwk5a5hpgyat8xtk2m3fdxa7ggamagum2ya3755p2gaae552pn1mawnprdr",
    "keyEncrypted": "amt4cwv48xb6pp1h5cw6jmtb9xk3jmhjf10m4dvu8xrn2j39c93n0ctb9wun6jjd61pkeh9raxtm2duk5cr6gxtgetc3gu2g9ruqgcaaf1mmcc3cdxapmhjp95q56due6xcpabvce91qgjhfe99pmx9pf1h4gatrd1m3cavqctm7et3ac4umcgb375j2ygba9nnpgpbnb5vpycv295c58h9na9m3cnbj6hmkadjgex43jhkc71tpunar8hc6mx2189pmeyhtdha6udam94yg",
    "customs": [],
    "attachments": [],
    "name": "API_ACCESS_KEY",
    "login": "",
    "url": "https://api.elk.com",
    "description": "",
    "tags": [],
    "fieldsOrder": null,
    "isDeleted": false,
    "color": 0,
    "isFavorite": false,
    "shortcut": {
        "id": "68d6c94bec3a3fe41209546e",
        "keyEncrypted": "amt4cwv48xb6pp1h5ww66ubecrnmcw346t8nmkue5dn5cu9mcn476xj59xcnjxa2en530dak8xmk0ukae9mmpgbad5a5ae2regrn4cahdd534rj95d65cp2r9h43ama3f9n46k2kd996guv9a4rqgm3bdhumecufa8w6mma3dhpmuju5enq6ry3de4t32hvjf5mq6c3ea9v62c1fa5kkauaab5vpjmbtcd0mmukk8cnpjduq9mv6rvbhc90nemjqe5gmaxk7dnp7eu3870yg",
        "itemId": "68793e13dfc88d879e0f2e39",
        "vaultId": "687663896eea6641b6065cd8",
        "folderId": null,
        "creator": "ldap_user_01"
    },
    "path": [
        {
            "name": "api_vaults_01",
            "vaultId": "687663896eea6641b6065cd8",
            "folderId": null
        }
    ],
    "password": {
        "id": "68793e13dfc88d879e0f2e39",
        "vaultId": "687663896eea6641b6065cd8",
        "folderId": null,
        "passwordEncrypted": "amt4cwv48xb6pp1h75wqacjha1kn0p328dn32tuuetrpuwk5a5hpgyat8xtk2m3fdxa7ggamagum2ya3755p2gaae552pn1mawnprdr",
        "keyEncrypted": "amt4cwv48xb6pp1h5cw6jmtb9xk3jmhjf10m4dvu8xrn2j39c93n0ctb9wun6jjd61pkeh9raxtm2duk5cr6gxtgetc3gu2g9ruqgcaaf1mmcc3cdxapmhjp95q56due6xcpabvce91qgjhfe99pmx9pf1h4gatrd1m3cavqctm7et3ac4umcgb375j2ygba9nnpgpbnb5vpycv295c58h9na9m3cnbj6hmkadjgex43jhkc71tpunar8hc6mx2189pmeyhtdha6udam94yg",
        "customs": [],
        "attachments": [],
        "name": "API_ACCESS_KEY",
        "login": "",
        "url": "https://api.elk.com",
        "description": "",
        "tags": [],
        "fieldsOrder": null,
        "isDeleted": false,
        "color": 0,
        "isFavorite": false,
        "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
        "password": "c4E*XU09:=([HY4462)4do"
    }
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `SHORTCUT_ID` of the shortcut to retrieve
3. The `get_shortcut()` method retrieves the shortcut and its associated item data
4. The shortcut and item are automatically decrypted using your master key
5. The response includes both shortcut metadata (location, creator) and the complete original item data
6. Optionally, you can download attachments from the shortcut

## Important Notes

- **Shortcut ID**: Required. Get it from the shortcut URL in the Passwork web interface
- **Master Key**: Required if client-side encryption is enabled. Both the shortcut and the original item will be automatically decrypted
- **Response Structure**: The response includes the shortcut metadata in the `shortcut` field and the complete original item data in the `password` field
- **Path Information**: The response includes a `path` array showing the vault/folder structure where the shortcut is located
- **Attachments**: If the shortcut (or original item) has attachments, you can download them using `download_shortcut_attachment()`. Uncomment the relevant line and provide a download path
- **Shortcut vs Item**: A shortcut is a reference to an item. Changes to the original item will be reflected in all shortcuts pointing to it
- **Permissions**: Ensure you have permission to access both the shortcut and the original item it references