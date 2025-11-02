# Getting Multiple Items

This example demonstrates how to retrieve and decrypt multiple items from Passwork using the Python connector.

## Use Case

You need to retrieve multiple items by their IDs in a single operation. This is more efficient than calling `get_item()` multiple times, as it retrieves all items in one batch request.

## Basic Usage

Create a file `get_items.py` with the following content:

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

# Example: Get multiple items
try:
    ITEM_IDS = ["6876652bb5613294cd0de807", "68793e13dfc88d879e0f2e39"]

    items = passwork.get_items(ITEM_IDS)
    print(f"Decrypted items: {items}")
except Exception as e:
    print(f"Error: {e}")
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving multiple items:

```shell
(api) passwork@api-integration:~# python3 get_items.py
[
    {
        "id": "6876652bb5613294cd0de807",
        "vaultId": "687663896eea6641b6065cd8",
        "folderId": null,
        "passwordEncrypted": "amt4cwv48xb6pp1h5wtppe2j85vq4ju9cd864vv1acqn6cuhedrq8nk79x64yma974u30f8",
        "keyEncrypted": "amt4cwv48xb6pp1h74nqan33d5un2cj3d1kqgm3dd9jk6c2j5x9q4nj5f9j58w3bb1gm6e2899566dk3b995ecvt5dr48jbtahkp2gvaecr3jp34exc5jwb464wmavkp6h72pt22a1umehb16cw6gp29f4umjvkmd8nk8jtnd4t52m3m9d364u1mf8v4ajj6dtum4hacdww3ew39atbmrtb8f8qpjuhhemt3gm9hc9kppdv99x7mawbmcmwm8h3p8thpemv4edm2pphjb4yg",
        "customs": [],
        "name": "administrator PROD",
        "login": "Administrator",
        "url": "https://administrator.com",
        "tags": [],
        "fieldsOrder": null,
        "isDeleted": false,
        "color": 0,
        "isFavorite": false,
        "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
        "password": "_=Xao_acB(SXes45i8R7L3"
    },
    {
        "id": "68793e13dfc88d879e0f2e39",
        "vaultId": "687663896eea6641b6065cd8",
        "folderId": null,
        "passwordEncrypted": "amt4cwv48xb6pp1h75wqacjha1kn0p328dn32tuuetrpuwk5a5hpgyat8xtk2m3fdxa7ggamagum2ya3755p2gaae552pn1mawnprdr",
        "keyEncrypted": "amt4cwv48xb6pp1h5cw6jmtb9xk3jmhjf10m4dvu8xrn2j39c93n0ctb9wun6jjd61pkeh9raxtm2duk5cr6gxtgetc3gu2g9ruqgcaaf1mmcc3cdxapmhjp95q56due6xcpabvce91qgjhfe99pmx9pf1h4gatrd1m3cavqctm7et3ac4umcgb375j2ygba9nnpgpbnb5vpycv295c58h9na9m3cnbj6hmkadjgex43jhkc71tpunar8hc6mx2189pmeyhtdha6udam94yg",
        "name": "database PROD",
        "login": "administrator",
        "url": "https://database.com",
        "customs": [],
        "tags": [],
        "fieldsOrder": null,
        "isDeleted": false,
        "color": 0,
        "isFavorite": false,
        "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
        "password": "uk-XhF%%vspIOt70(PYF+="
    }
]
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies a list of `ITEM_IDS` for the items to retrieve
3. The `get_items()` method retrieves all specified items in a single batch request
4. All items are automatically decrypted using your master key
5. The method returns a list of decrypted items with all fields accessible
6. This approach is more efficient than calling `get_item()` multiple times

## Important Notes

- **Item IDs**: Required. Provide a list of item IDs you want to retrieve
- **Batch Operation**: This method retrieves multiple items in a single request, which is more efficient than individual requests
- **Master Key**: Required if client-side encryption is enabled. All items will be automatically decrypted using your master key
- **Response Format**: Returns a list of item dictionaries, each containing all item fields and metadata
- **Permissions**: Ensure you have permission to access all items in the list and their respective vaults
- **Partial Success**: If some items cannot be retrieved (due to permissions or missing items), the method will return only the accessible items
- **Performance**: Use `get_items()` when you need multiple items instead of calling `get_item()` in a loop for better performance