# Creating a Link

This example demonstrates how to create a shareable link for an item or shortcut in Passwork using the Python connector.

## Use Case

You need to create a shareable link to an item or shortcut that can be accessed without direct Passwork authentication. Links can be reusable or single-use, and can have different expiration times.

## Basic Usage

Create a file `create_link.py` with the following content:

```python
from passwork_client import PassworkClient
from passwork_client.constants.link_type import LinkType
from passwork_client.constants.link_expiration_time import LinkExpirationTime

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

# Example: Create link
try:
    ITEM_ID = "68d3cf81473b357ee60a66cd"
    SHORTCUT_ID = None

    link = passwork.create_link(LinkType.Reusable, LinkExpirationTime.Unlimited, ITEM_ID, SHORTCUT_ID)
    print(f"Link: {link}")
except Exception as e:
    print(f"Error: {e}")
```

Description:
- Put the item ID or shortcut ID for creating the link into the `ITEM_ID` or `SHORTCUT_ID` values. You can get the item ID or shortcut ID by opening the Passwork web interface, selecting an item or shortcut, and the ID will be displayed in the address bar, for example: `https://passwork.example.org/p/68d3cf81473b357ee60a66cd`

- The `LinkType` parameter determines the link type. Reusable(`Reusable`)/Single-use(`Single_use`)

- The `LinkExpirationTime` parameter determines the link expiration time. 1 hour(`Hour`)/1 week(`Week`)/1 month(`Month`)/Unlimited(`Unlimited`)

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating a link:

```shell
(api) passwork@api-integration:~# python3 create_link.py
Link: https://passwork.example.org/g/p/KLul6UwnSD28DvvCYtjfgUnlb#code=2qUVLLinLAVU8kzILckD0GH5ptGmK5fBEICmLG3CwrLapdM3h8yd0GimP9Qz7dERgX@E8RHDLQgOn8mZRceLgnhMiY0hTtVLWJHr
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It specifies either an `ITEM_ID` or `SHORTCUT_ID` (but not both)
3. The link type is set using `LinkType` (Reusable or Single_use)
4. The expiration time is set using `LinkExpirationTime` (Hour, Week, Month, or Unlimited)
5. A shareable link is created and returned as a URL
6. The link can be shared with others who don't need Passwork authentication to access the item or shortcut

## Important Notes

- **Item ID or Shortcut ID**: Required. You must provide either `ITEM_ID` or `SHORTCUT_ID`, but not both. Set the unused one to `None`
- **Link Type**: Choose `LinkType.Reusable` for links that can be used multiple times, or `LinkType.Single_use` for one-time access links
- **Expiration Time**: Choose from `LinkExpirationTime.Hour`, `LinkExpirationTime.Week`, `LinkExpirationTime.Month`, or `LinkExpirationTime.Unlimited`
- **Getting IDs**: Item and shortcut IDs can be found in the URL when viewing them in the Passwork web interface
- **Link Format**: The created link includes a unique code that grants access without authentication