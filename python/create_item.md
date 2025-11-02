# Creating an Item

This example demonstrates how to create a new item in Passwork using the Python connector.

## Use Case

You need to create a new item with login credentials, URL, description, tags, and custom fields. Items can include standard fields (name, login, password, URL, description) as well as custom fields for storing additional information.

## Basic Usage

Create a file `create_item.py` with the following content:

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

# Example: Create item
try:
    VAULT_ID = "68d3c3b3473b357ee60a66b8"
    
    # Example custom fields
    custom_fields = [
        {
            "name": "Text Field",
            "value": "Field value",
            "type": "text"
        },
        {
            "name": "Custom Password",
            "value": "Secret123!",
            "type": "password"
        },
        {
            "name": "TOTP",
            "value": "ABCDEFGHIJKLMNOP",
            "type": "totp"
        }
    ]
    
    # Prepare item data
    item_data = {
        "vaultId": VAULT_ID,
        "name": "Grafana Access",
        "login": "ldap_view_grafana@passwork.local",
        "password": "P@ssw0rd",
        "url": "https://grafana.passwork.com",
        "description": "Item description",
        "tags": ["grafana", "monitoring"],
        "customs": custom_fields
    }
    
    # Create item
    item_id = passwork.create_item(item_data)
    print(f"Item created with ID: {item_id}")
    
    # Get the created item
    item = passwork.get_item(item_id)
    print(f"Created item: {item}")

except Exception as e:
    print(f"Error: {e}") 
```

Description:
- Put the vault ID where the item will be created into the `VAULT_ID` value. You can get the vault ID by opening the Passwork web interface, selecting a vault, and the ID will be displayed in the address bar, for example: `https://passwork.example.org/68d3c3b3473b357ee60a66b8`

- If you don't plan to create custom fields, remove the `custom_fields` array and remove the `customs` field with its value from `item_data`

- If you don't need to output the created item, comment out `item = passwork.get_item(item_id)` and `print(f"Created item: {item}")`

</details>

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating an item:

```shell
(api) passwork@api-integration:~# python3 create_item.py 
Item created with ID: 68d3d19c3ea6febf700c740a
{
  "id": "68d3d19c3ea6febf700c740a",
  "vaultId": "68d3c3b3473b357ee60a66b8",
  "folderId": null,
  "passwordEncrypted": "amt4cwv48xb6pp1h7564uuku8d44era25dn66ja39dhqcta4ddm6wy3m6dnpck36dgqm2f8",
  "keyEncrypted": "amt4cwv48xb6pp1h5xcqgcvr6gtq0xu3ehnk2v396993ayjt5wqpyxv1c586gtb8axk7mxvb84tm8thpd0rkcnk79hmn0nub9ntpyrv5b1n7jcu4c5r68x399xwnevupc8wpghbra5n7mhjp9x1n4cjgb9aqcnjhb566mm2u69ck0rucf5j4mjhf8t5myrbmctt4wp9ba5nkjmjc70qqmhubahu7acb48ha3crjj6t4pet3pf97ppx33b8w38rj7ehtqjxj2edupry3nb4yg",
  "customs": [
    {
      "name": "Text Field",
      "value": "Field value",
      "type": "text"
    },
    {
      "name": "Custom Password",
      "value": "Secret123!",
      "type": "password"
    },
    {
      "name": "TOTP",
      "value": "ABCDEFGHIJKLMNOP",
      "type": "totp"
    }
  ],
  "attachments": [],
  "name": "Grafana Access",
  "login": "ldap_view_grafana@passwork.local",
  "url": "https://grafana.passwork.com",
  "description": "Item description",
  "tags": [
    "grafana",
    "monitoring"
  ],
  "fieldsOrder": null,
  "isDeleted": false,
  "color": 0,
  "isFavorite": false,
  "vaultMasterKeyEncrypted": "YTn1XiFjvaF8ijSFZe3rqGvEjboMD9bwWm2ssviZg/jb9cJQXbBcceVm+Fga7ZcIqWKHBe/SncGgfyAqMCJr+Hm49mqVCfoyMxX/euYU8qRnxXHys1A9HIJRsCbJnrS3i+t6+FWwuXwHRb/wLQYnGMP5G086BT8OmBTu4dBaNHkHfn2RNzo8OurrXczyPjNl6RBOL9BngbL4rGaGftCOpc2kuVHNS3DJkZi5k5L1OiOGkV04l5quLwOzqBZLozlzVx7WREZQansRgsXTEGEwNdxHrXgfl1HX4jpmWCl3CYFf/xK3vPrGvg78keio7fT/scDf3mgnYIy3KuwJFrMftg==",
  "password": "P@ssw0rd"
}
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It prepares item data including standard fields (name, login, password, URL, description) and custom fields
3. Custom fields can be of different types: text, password, or TOTP
4. The item is created in the specified vault using `create_item()`
5. Optionally, the created item can be retrieved and displayed to verify the creation

## Important Notes

- **Vault ID**: Required. Get it from the web interface by viewing the vault URL
- **Custom Fields**: Optional. Remove the `custom_fields` array and `customs` field if not needed
- **Item Retrieval**: The script retrieves and prints the created item by default. Comment out those lines if not needed
- **Field Types**: Supported custom field types include: `text`, `password`, `totp`
- **Tags**: Provide tags as a list of strings