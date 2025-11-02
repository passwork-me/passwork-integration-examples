# Creating a User

This example demonstrates how to create a new local user in Passwork using the Python connector.

## Use Case

You need to programmatically create a new local user account in Passwork. This is useful for automation, bulk user creation, or integration with other user management systems.

## Basic Usage

Create a file `create_user.py` with the following content:

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

# Example: Create user
try:
    # Get available user roles
    roles_response = passwork.call("GET", "/api/v1/user-roles", {"includeUserRole": '1', "isOnlyManageable": '1'})
    if not roles_response or not roles_response.get("items"):
        print("Error: Could not fetch user roles or no manageable roles found.")
        exit(1)

    # Find the 'user' role (adjust if needed)
    user_role_items = [r for r in roles_response["items"] if r.get("code") == "user"]
    if not user_role_items:
        print("Error: Default 'user' role not found.")
        exit(1)
    default_user_role_id = user_role_items[0]["id"]
    
    # Fill user data
    user_data = {
        "email": "create_python_user@example.com",
        "fullName": "Python Test User",
        "login": "create_python_user",
        "userRoleId": default_user_role_id,
        # "userGroupIds": [], 
    }
    
    # Create user
    new_user = passwork.create_user(user_data)

    # Construct success message
    message = f"User '{user_data['fullName']}' created with ID: {new_user['user_id']}"
    if 'password' in new_user and new_user['password']:
         message += f", password: {new_user['password']}"
    if 'master_password' in new_user and new_user['master_password']:
        message += f", master password: {new_user['master_password']}"

    print(message)

except Exception as e:
    print(f"Error: {e}") 
```

Description:
- The `email` parameter sets the email field value for the user being created

- The `fullName` parameter specifies the full name of the user (for example, First Name Last Name or First Name)

- The `login` parameter specifies the login for authentication in Passwork

- The `userRoleId` parameter sets the user role (default is **Employee**)

- The `userGroupIds` parameter specifies the groups to which the user belongs (one or more)

Insert the tokens obtained from the web interface (user master key, if client-side encryption is enabled) into the script and save it. Example of running the script and successfully creating a user:

```shell
(api) passwork@api-integration:~# python3 create_user.py 
User 'Python Test User' created with ID: 68da4cf1bf68ddc3b80d2342, password: JhUaUIcIK8If, master password: XBcO5sAE$HL7
```

## How It Works

1. The script initializes the PassworkClient and authenticates using tokens
2. It fetches available user roles from the API to find manageable roles
3. It searches for the default "user" role (Employee role) by its code
4. User data is prepared including email, full name, login, and role ID
5. Optionally, user groups can be specified (commented out in the example)
6. A new user is created with the specified data
7. The script displays the created user ID along with the generated password and master password (if provided)

## Important Notes

- **Email**: Required. Must be a valid email address and unique within the Passwork instance
- **Full Name**: Required. The display name for the user
- **Login**: Required. Must be unique and used for authentication
- **User Role**: Required. The script automatically finds the default "user" role (Employee), but you can modify the search to use a different role
- **User Groups**: Optional. Uncomment `userGroupIds` and provide a list of group IDs if you want to assign the user to specific groups
- **Generated Passwords**: The system automatically generates a password and master password for the new user. These are returned in the response and should be securely communicated to the user
- **Permissions**: Ensure your API token has sufficient permissions to create users

