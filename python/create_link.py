from passwork_client import PassworkClient
from passwork_client.constants.link_type import LinkType
from passwork_client.constants.link_expiration_time import LinkExpirationTime

# Configuration
ACCESS_TOKEN = ""
REFRESH_TOKEN = "" # Optional (if you need to refresh access token)
MASTER_KEY = "" # Master key (if client side encryption is enabled)
HOST = "https://passwork" # Passwork host


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
    ITEM_ID = None
    SHORTCUT_ID = None

    link = passwork.create_link(LinkType.Reusable, LinkExpirationTime.Unlimited, ITEM_ID, SHORTCUT_ID)
    print(f"Link: {link}")
except Exception as e:
    print(f"Error: {e}")