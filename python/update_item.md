# Updating an Item

This example demonstrates how to update an item in Passwork using the Python connector.

## Use Case

You need to update an existing item with new values for fields such as name, login, password, URL, description, tags, or custom fields. This is useful for maintaining up-to-date credentials and information.

## Basic Usage

Create a file `update_item.py` with the following content:

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

# Example: Update item
try:
    # ID of the item to update
    ITEM_ID = "68793e13dfc88d879e0f2e39"
    # ID of the vault where the item is located
    VAULT_ID = "687663896eea6641b6065cd8"
    
    # Get current item
    item = passwork.get_item(ITEM_ID)
    print(f"Current item: {item}")
    
    # Prepare updated data
    updated_data = {
        "vaultId": VAULT_ID,
        "name": "Updated Item Name",
        "login": "updated_user",
        "password": "Updated_Password_456!",
        "url": "https://updated-example.com",
        "description": "Updated description",
        "tags": ["updated", "tag2", "tag3"],
        "customs": [
            {
                "name": "Updated Custom Field",
                "value": "Updated value",
                "type": "text"
            },
            {
                "name": "Updated Password Field",
                "value": "NewSecret456!",
                "type": "password"
            }
        ]
    }
    
    # Update the item
    passwork.update_item(ITEM_ID, updated_data)
    
    # Get the updated item
    updated_item = passwork.get_item(ITEM_ID)
    print(f"Updated item: {updated_item}")

except Exception as e:
    print(f"Error: {e}") 
```

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully updating an item:

```shell
(api) passwork@api-integration:~# python3 update_item.py 
{
    "id": "68793e13dfc88d879e0f2e39",
    "vaultId": "687663896eea6641b6065cd8",
    "folderId": null,
    "passwordEncrypted": "amt4cwv48xb6pp1h5xn6mxhqa1h6uruhdt2pyy2ue1t76y3799p5jtkpa9p56hv59x84euuhd9vk4dace0nqgxau8t9qmt266x26yg8",
    "keyEncrypted": "amt4cwv48xb6pp1h5dh6amvbcnmkjhjtcd9pwm2hb5952wb88hd5mhvrf92pmn268dr4pgvg8x55jyhpanvprhve718m6dbqdh83jyb7dxupyd2ka9544r9q8hv4mhjd99p6gt3hdn16rybde15kartka1w52cjbedqqax3eb176gpb471kpjxjm6nk6gv1q8nr68hbrcgr7ak2meh9n0vb8chv56kaed5umreb99hkmmy9b6586jkkuddhjpmk2ahj6gnb6cd6mgj2294yg",
    "customs": [
        {
            "name": "Updated Custom Field",
            "value": "Updated value",
            "type": "text"
        },
        {
            "name": "Updated Password Field",
            "value": "NewSecret456!",
            "type": "password"
        }
    ],
    "attachments": [],
    "name": "Updated Item Name",
    "login": "updated_user",
    "url": "https://updated-example.com",
    "description": "Updated description",
    "tags": [
        "updated",
        "tag2",
        "tag3"
    ],
    "fieldsOrder": null,
    "isDeleted": false,
    "color": 0,
    "isFavorite": false,
    "vaultMasterKeyEncrypted": "oUn96mdysy5Pw7W9r3Ss0Gv1gd54jh0cmTVQrxhI5OkseptPGVZFdd6TaswgqjFOwS1WS1Ail8Tu82XNn346VBYsZ19z5bltKXJelwfedoQwTwIPFABC/u9hHt2HOGiSh6hBE2bpFzN376qFm9IpFN5xXmFydXB2tN+EbklCLngEERRmNgxlImaeq/O2tgwvn/kZkHROK7d/Bnd7/jMcEeekX0jTJBVg78BMHOdb+whOLr5dhZIyAI1pi9kzLnxzoE9oAKTV8mQe+eXhBWjgI5LXb++0Oghua3EbY2prndNU6ZuUDbQBO/3zeTlfXIr27V8q7I2msspJulJP5lpVfw==",
    "password": "Updated_Password_456!"
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It retrieves the current item using `get_item()` to see its current state
3. It prepares updated data with new values for any fields you want to change
4. The `update_item()` method updates the item with the new data
5. All specified fields are replaced with the new values
6. Custom fields can be updated or added
7. Tags are replaced with the new list
8. The updated item can be retrieved to verify the changes

## Important Notes

- **Item ID**: Required. The ID of the item you want to update
- **Vault ID**: Required. The ID of the vault where the item is located
- **Field Updates**: All fields in `updated_data` will replace the corresponding fields in the item
- **Partial Updates**: You only need to include fields you want to update.
- **Custom Fields**: Custom fields can be updated by providing the field name, value, and type. Existing custom fields not in the update will be removed
- **Tags**: The tags list completely replaces existing tags. Provide all tags you want to keep
- **Password Update**: Passwords are automatically encrypted when saved
- **Permissions**: Ensure you have edit permission for the item and access to the vault
- **Verification**: The script retrieves the updated item after update to verify changes were applied correctly