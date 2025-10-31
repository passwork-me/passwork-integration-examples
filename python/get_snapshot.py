import os
from passwork_client import PassworkClient

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

# Example: Get snapshot
try:
    ITEM_ID = ""
    SNAPSHOT_ID = ""
    DOWNLOAD_PATH = os.path.join("./attachments", SNAPSHOT_ID)

    snapshot = passwork.get_snapshot(ITEM_ID, SNAPSHOT_ID)
    #passwork.download_snapshot_attachments(snapshot, DOWNLOAD_PATH)
    print(f"Decrypted item: {snapshot}")
except Exception as e:
    print(f"Error: {e}")