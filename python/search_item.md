# Searching Items

This example demonstrates how to search for items in Passwork using the Python connector with automatic decryption.

## Use Case

You need to search for items by tags, folders, vaults, or text query. The search results are automatically decrypted, allowing you to access all fields including passwords immediately.

## Basic Usage

Create a file `search_item.py` with the following content:

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

# Example: Search items
try:
    tags = [] # Optional
    folders = [] # Optional
    vaults = [] # Optional
    search_query = "Prometheus" # Optional
    
    items = passwork.search_and_decrypt(tags=tags, folder_ids=folders, vault_ids=vaults, query=search_query)
    print(f"Decrypted items: {items}")
except Exception as e:
    print(f"Error: {e}")
```

Description:
- The `tags` parameter searches for items containing specific tags (one or more), example: `tags = ["passwork", "postgresql"]`

- The `folders` parameter searches in specific folder(s) (search does not include subfolders), example: `folders = ["68dd0540f21ee0493f07614a", "68dd0572f21ee0493f07614d"]`

- The `vaults` parameter searches for items in vault(s) (search includes folders and subfolders), example: `vaults = ["687663896eea6641b6065cd8", "68d835957229742928084234"]`

- The `search_query` parameter searches items by: item name, URL address, or notes, example: `search_query = "Prometheus"`

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully searching for items:

```shell
(api) passwork@api-integration:~# python3 search_item.py 
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
        "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
        "password": "H2.V4g(xKYR]%gOByjj~gF"
    }
]
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies search criteria using optional parameters:
   - `tags`: Filter by one or more tags
   - `folders`: Search within specific folders (not subfolders)
   - `vaults`: Search within specific vaults (includes folders and subfolders)
   - `query`: Search by item name, URL, or description
3. The `search_and_decrypt()` method performs the search and automatically decrypts all found items
4. All matching items are returned as a list with all fields accessible, including passwords
5. You can combine multiple search criteria to narrow down results

## Important Notes

- **All Parameters Optional**: All search parameters are optional. You can use any combination of them
- **Tags**: Provide a list of tag names to search for items containing those tags
- **Folders**: Search is limited to the specified folders only (does not include subfolders)
- **Vaults**: Search includes all folders and subfolders within the specified vaults
- **Search Query**: Searches item names, URLs, and descriptions. This is a text-based search
- **Automatic Decryption**: All found items are automatically decrypted using your master key
- **Combining Criteria**: You can combine tags, folders, vaults, and query for more precise searches
- **Empty Lists**: Use empty lists `[]` if you don't want to filter by that criteria
- **Permissions**: Results only include items you have permission to access