# Getting a Snapshot

This example demonstrates how to retrieve and decrypt a snapshot (Editions) of an item in Passwork using the Python connector.

## Use Case

You need to retrieve a specific snapshot (Editions) of an item. Snapshots preserve the state of an item at a particular point in time, allowing you to view or restore previous versions of the item.

## Basic Usage

Create a file `get_snapshot.py` with the following content:

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

# Example: Get snapshot
try:
    ITEM_ID = "68da8894f28bf56cec08c55e"
    SNAPSHOT_ID = "68da8894f28bf56cec08c560"
    DOWNLOAD_PATH = os.path.join("./attachments", SNAPSHOT_ID)

    snapshot = passwork.get_snapshot(ITEM_ID, SNAPSHOT_ID)
    # If you need to download attachments from the snapshot
    #passwork.download_snapshot_attachments(snapshot, DOWNLOAD_PATH)
    print(f"Decrypted item: {snapshot}")
except Exception as e:
    print(f"Error: {e}")
```

Description:
- The `ITEM_ID` parameter specifies the item from which to retrieve the snapshot. You can get the item ID by opening the Passwork web interface, selecting an item, and the ID will be displayed in the address bar, for example: `https://passwork.example.org/p/68d3cf81473b357ee60a66cd`

- The `SNAPSHOT_ID` parameter specifies the ID of the snapshot to retrieve from the item

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully retrieving a snapshot:

```shell
(api) passwork@api-integration:~# python3 get_snapshot.py 
{
    "id": "68da8894f28bf56cec08c560",
    "itemId": "68da8894f28bf56cec08c55e",
    "name": "Prometheus PROD",
    "login": "administrator",
    "passwordEncrypted": "amt4cwv48xb6pp1h5x6p2kjja1h7cvvfcx6n0n268rrmup9t99d3ebu2e174erj99hp62tk58h254u2p6126cujne9jngavq6x46mnr",
    "url": "https://prom.passwork.com",
    "customs": [],
    "tags": [
        "passwork",
        "prometheus"
    ],
    "attachments": [],
    "creatorId": "6874f2180c7799f6d5058707",
    "createdAt": 1759152276,
    "keyEncrypted": "amt4cwv48xb6pp1h74t5ak346nnpytjhegvmmra59ngp6wkk712myp2764v76pa7aha6rdbaan6pegjbchq3arj1c5kqmx3fdt1p2kbu750k4xthemu62nvfct5mentt896p4kvg6tupgx9q6wv4ubvje95p8btfb1vqgn339xmn2mkne59p2m2b5dbpjmktd59k6tata1x38jkrct7q2kun5xr36gv18cv6wdbnf1a68tj79dv58whrcnp4mgade1rqmvb5ctjmec3584yg",
    "description": null,
    "fieldsOrder": null,
    "creator": {
        "id": "6874f2180c7799f6d5058707",
        "login": "admin",
        "fullName": "Administrator",
        "hasAvatar": false,
        "isDeleted": false
    },
    "password": "H2.V4g(xKYR]%gOByjj~gF"
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies both the `ITEM_ID` of the item and the `SNAPSHOT_ID` of the specific snapshot to retrieve
3. The `get_snapshot()` method retrieves the edition version of the item
4. The snapshot is automatically decrypted using your master key
5. The response includes all item fields as they were at the time of the snapshot, plus metadata about when it was created and by whom
6. Optionally, you can download attachments from the snapshot

## Important Notes

- **Item ID**: Required. The ID of the item whose snapshot you want to retrieve
- **Snapshot ID**: Required. The ID of the specific snapshot (edition) to retrieve. Get it from the item's version history
- **Master Key**: Required if client-side encryption is enabled. The snapshot will be automatically decrypted using your master key
- **Historical Data**: Snapshots preserve the state of an item at a specific point in time, including all fields and values
- **Creator Information**: The response includes information about who created the snapshot and when (`createdAt` timestamp)
- **Attachments**: If the snapshot has attachments, you can download them using `download_snapshot_attachments()`. Uncomment the relevant line and provide a download path
- **Edition History**: Each time an item is modified, a new snapshot is created automatically
- **Permissions**: Ensure you have permission to access both the item