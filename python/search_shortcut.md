# Searching Shortcuts

This example demonstrates how to search for shortcuts in Passwork using the Python connector with automatic decryption.

## Use Case

You need to search for shortcuts by tags, folders, vaults, or text query. Shortcuts are references to items that can be placed in different vaults or folders. The search results are automatically decrypted, allowing you to access all fields including passwords immediately.

## Basic Usage

Create a file `search_shortcut.py` with the following content:

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

# Example: Search shortcuts
try:
    tags = [] # Optional
    folders = [] # Optional
    vaults = [] # Optional
    search_query = "Prometheus" # Optional

    shortcuts = passwork.search_and_decrypt_shortcut(tags=tags, query=search_query, vault_ids=vaults, folder_ids=folders)
    print(f"Decrypted shortcuts: {shortcuts}")
except Exception as e:
    print(f"Error: {e}")
```

Description:
- The `tags` parameter searches for shortcuts containing specific tags (one or more), example: `tags = ["passwork", "postgresql"]`

- The `folders` parameter searches in specific folder(s) (search does not include subfolders), example: `folders = ["68dd0540f21ee0493f07614a", "68dd0572f21ee0493f07614d"]`

- The `vaults` parameter searches for shortcuts in vault(s) (search includes folders and subfolders), example: `vaults = ["687663896eea6641b6065cd8", "68d835957229742928084234"]`

- The `search_query` parameter searches shortcuts by: shortcut name, URL address, or notes, example: `search_query = "Prometheus"`

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully searching for shortcuts:

```shell
(api) passwork@api-integration:~# python3 search_shortcut.py 
[
    {
        "id": "68da8894f28bf56cec08c55e",
        "vaultId": "687663896eea6641b6065cd8",
        "folderId": null,
        "passwordEncrypted": "amt4cwv48xb6pp1h5d3pcvkuahqm2jje8xpp2daj6ct5gxu3anqmuujeb90m4y1fdtm4mjbkehuqgvk2cham8uv4b535jujea9tmygr",
        "keyEncrypted": "amt4cwv48xb6pp1h74t5ak346nnpytjhegvmmra59ngp6wkk712myp2764v76pa7aha6rdbaan6pegjbchq3arj1c5kqmx3fdt1p2kbu750k4xthemu62nvfct5mentt896p4kvg6tupgx9q6wv4ubvje95p8btfb1vqgn339xmn2mkne59p2m2b5dbpjmktd59k6tata1x38jkrct7q2kun5xr36gv18cv6wdbnf1a68tj79dv58whrcnp4mgade1rqmvb5ctjmec3584yg",
        "customs": [],
        "attachments": [],
        "name": "Prometheus DEV",
        "login": "administrator",
        "url": "https://prom.passwork.com",
        "description": null,
        "tags": [
            "passwork",
            "prometheus"
        ],
        "fieldsOrder": null,
        "isDeleted": false,
        "color": 0,
        "isFavorite": false,
        "shortcut": {
            "id": "68da954cdca4afe4d1047ac4",
            "keyEncrypted": "amt4cwv48xb6pp1h70ummgam6t35gh2batn5av26a51q6nhm9nr4gkhnadhn4d366x27jnbd8xgqjca9anvnexu88577gv1g5dm2yna3dmumup2e8h944xk99rupuaupah6nmkaub5vjph3de52pwh259nd4jp1h61m30d32ax476d2hb9ap2av971n6yuvd6t1k0mu89926cj1pf59k6j9f719q2wuratrkgxthdn42pe2pe0nq8x1hat9k8vbp75w76e1fa9ummvj18myg",
            "itemId": "68da8894f28bf56cec08c55e",
            "vaultId": "6879fb0d62b875b016026bb4",
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
            "id": "68da8894f28bf56cec08c55e",
            "vaultId": "687663896eea6641b6065cd8",
            "folderId": null,
            "passwordEncrypted": "amt4cwv48xb6pp1h5d3pcvkuahqm2jje8xpp2daj6ct5gxu3anqmuujeb90m4y1fdtm4mjbkehuqgvk2cham8uv4b535jujea9tmygr",
            "keyEncrypted": "amt4cwv48xb6pp1h74t5ak346nnpytjhegvmmra59ngp6wkk712myp2764v76pa7aha6rdbaan6pegjbchq3arj1c5kqmx3fdt1p2kbu750k4xthemu62nvfct5mentt896p4kvg6tupgx9q6wv4ubvje95p8btfb1vqgn339xmn2mkne59p2m2b5dbpjmktd59k6tata1x38jkrct7q2kun5xr36gv18cv6wdbnf1a68tj79dv58whrcnp4mgade1rqmvb5ctjmec3584yg",
            "customs": [],
            "attachments": [],
            "name": "Prometheus DEV",
            "login": "administrator",
            "url": "https://prom.passwork.com",
            "description": null,
            "tags": [
                "passwork",
                "prometheus"
            ],
            "fieldsOrder": null,
            "isDeleted": false,
            "color": 0,
            "isFavorite": false,
            "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
            "password": "H2.V4g(xKYR]%gOByjj~gF"
        }
    }
]
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies search criteria using optional parameters:
   - `tags`: Filter by one or more tags
   - `folders`: Search within specific folders (not subfolders)
   - `vaults`: Search within specific vaults (includes folders and subfolders)
   - `query`: Search by shortcut name, URL, or description
3. The `search_and_decrypt_shortcut()` method performs the search and automatically decrypts all found shortcuts
4. Each result includes both shortcut metadata (in the `shortcut` field) and the complete original item data (in the `password` field)
5. All fields are accessible, including passwords

## Important Notes

- **All Parameters Optional**: All search parameters are optional. You can use any combination of them
- **Tags**: Provide a list of tag names to search for shortcuts containing those tags
- **Folders**: Search is limited to the specified folders only (does not include subfolders)
- **Vaults**: Search includes all folders and subfolders within the specified vaults
- **Search Query**: Searches shortcut names, URLs, and descriptions. This is a text-based search
- **Automatic Decryption**: All found shortcuts are automatically decrypted using your master key
- **Response Structure**: Each result includes shortcut metadata (`shortcut` field) and the complete original item data (`password` field)
- **Combining Criteria**: You can combine tags, folders, vaults, and query for more precise searches
- **Empty Lists**: Use empty lists `[]` if you don't want to filter by that criteria
- **Permissions**: Results only include shortcuts you have permission to access