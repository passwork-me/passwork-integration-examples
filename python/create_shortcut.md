# Creating a Shortcut

This example demonstrates how to create a shortcut to an item in Passwork using the Python connector.

## Use Case

You need to create a shortcut to an existing item in a different vault or folder. Shortcuts allow you to reference the same item from multiple locations without duplicating the item data.

## Basic Usage

Create a file `create_shortcut.py` with the following content:

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

# Example: Create shortcut
try:
    ITEM_ID = "6876652bb5613294cd0de807"
    VAULT_ID = "687663896eea6641b6065cd8"
    FOLDER_ID = None

    shortcut_id = passwork.create_shortcut(ITEM_ID, VAULT_ID, FOLDER_ID) 

    print(f"Shortcut was created: {shortcut_id}") 

except Exception as e:
    print(f"Error: {e}") 
```

Description:
- The `ITEM_ID` parameter specifies the item for creating a shortcut. You can get the item ID by opening the Passwork web interface, selecting an item, and the ID will be displayed in the address bar, for example: `https://passwork.example.org/p/68d3cf81473b357ee60a66cd`

- The `VAULT_ID` parameter specifies in which vault the shortcut will be created

- The `FOLDER_ID` parameter specifies in which folder of the vault the shortcut will be created

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating a shortcut:

```shell
(api) passwork@api-integration:~# python3 create_shortcut.py 
Shortcut was created: 68da4849c9294fee52018fa2
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies the `ITEM_ID` of the original item to create a shortcut to
3. It specifies the `VAULT_ID` where the shortcut will be created
4. Optionally, it can specify a `FOLDER_ID` if the shortcut should be placed in a specific folder (set to `None` for vault root)
5. A shortcut is created that references the original item
6. The shortcut ID is returned and can be used to access the item from the new location

## Important Notes

- **Item ID**: Required. The ID of the original item you want to create a shortcut to. Get it from the item URL in the web interface
- **Vault ID**: Required. The ID of the vault where you want to place the shortcut. This can be different from the vault containing the original item
- **Folder ID**: Optional. Set to `None` to create the shortcut in the vault root, or provide a folder ID to place it in a specific folder
- **Shortcut vs Item**: A shortcut is a reference to an item, not a copy. Changes to the original item will be reflected in all shortcuts
- **Access Permissions**: Ensure you have permission to create shortcuts in the target vault

