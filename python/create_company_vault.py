from passwork_client import PassworkClient
from passwork_client.exceptions import PassworkError

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

# Example: Create company vault
try:
    vault_name = "Python Vault"
    company_vault_type = passwork.find_vault_type(code="company")
    if not company_vault_type:
        raise PassworkError("Default 'company' vault type not found.")

    vault_id = passwork.create_vault(vault_name, company_vault_type["id"])
    print(f"Vault was created: {vault_id}")
except Exception as e:
    print(f"Error: {e}")