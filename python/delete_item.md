# Deleting an Item

This example demonstrates how to delete an item in Passwork using the Python connector.

## Use Case

You need to delete an item from Passwork. When an item is deleted, it is moved to the bin (trash) and can be restored if needed.

## Basic Usage

Create a file `delete_item.py` with the following content:

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

# Example: Delete item
try:
    # ID of the item to delete
    ITEM_ID = "68d8377954f0c66ba70cf40b"
    
    # Delete the item
    bin_item_id = passwork.delete_item(ITEM_ID)
    print(f"Item deleted. Bin item ID: {bin_item_id}")
    
except Exception as e:
    print(f"Error: {e}")
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully deleting an item:

```shell
(api) passwork@api-integration:~# python3 delete_item.py 
Item deleted. Bin item ID: 68da5451bf68ddc3b80d2344
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `ITEM_ID` of the item to delete
3. The item is deleted using the `delete_item()` method
4. The deleted item is moved to the bin (trash)
5. The bin item ID is returned, which can be used to restore the item if needed

## Important Notes

- **Item ID**: Required. The ID of the item you want to delete. Get it from the item URL in the web interface
- **Bin/Trash**: Deleted items are moved to the bin, not permanently removed immediately
- **Restoration**: Items in the bin can be restored using the bin item ID if needed
- **Permissions**: Ensure you have permission to delete the item
- **Permanent Deletion**: Items in the bin may be permanently deleted after a retention period