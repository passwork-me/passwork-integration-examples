# Getting items and shortcuts

This example demonstrates how to retrieve items and shortcuts from Passwork using the `get` command, and how to extract specific fields from them.

## Use cases

1. **Retrieve the full password object** - Get all information about a item or shortcut
2. **Extract specific fields** - Get only the password, login, URL, description, tags, or custom fields
3. **Use in scripts** - Get password values for use in automation scripts

## Basic usage

### Get password value item by ID

```bash
passwork-cli get \
  --host "https://passwork.example.com" \
  --token "your_access_token" \
  --master-key "your_master_key" \
  --password-id "68793e13dfc88d879e0f2e39" \
```

This will output the password value by default. If the password field is empty, an error will be displayed.

## SSL parameters

Use the `--ssl-verify` parameter to control SSL certificate verification:

```bash
# Use system certificate store explicitly
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --ssl-verify

# Use a custom CA bundle or certificate directory
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --ssl-verify "/etc/ssl/certs"
```

You can also use `--no-ssl-verify`:

```bash
# Disable SSL verification
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --no-ssl-verify
```

## Extracting specific fields

You can extract specific fields from a password or shortcut using the `--field` parameter.

### Standard fields

```bash
# Get item name
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field name
# Get login
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field login
# Get password value
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field password
# Get description
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field description
# Get URL
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field url
# Get tags (comma-separated)
passwork-cli get --password-id "687515386b432f24150366b7" --field tags
```

### Custom fields

You can also extract custom fields by specifying their name:

```bash
# Get a text custom field
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field text_field
# Get a custom password field (e.g., API_KEY)
passwork-cli get --password-id "68793e13dfc88d879e0f2e39" --field API_KEY
```

## Generating TOTP codes

You can generate TOTP (Time-based One-Time Password) codes from secrets stored in custom fields. This is useful for two-factor authentication.

### Using TOTP secret field

```bash
# Generate TOTP code from a custom field containing the secret
passwork-cli get \
  --password-id "68793e13dfc88d879e0f2e39" \
  --totp-code "TOTP_SECRET" \
```

The `--totp-code` parameter expects the name of a field (custom) that contains:
- A raw TOTP secret (base32 encoded string)
- Or an `otpauth://` URL (e.g., `otpauth://totp/Service:user@example.com?secret=JBSWY3DPEHPK3PXP&issuer=Service`)

The TOTP code will be printed to stdout, making it easy to use in scripts or copy for authentication.

### Working with shortcuts

The same field extraction works for shortcuts:

```bash
# Get password shortcut
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e"
```

Extract specific fields from shortcut:

```bash
# Get item name
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field name
# Get login
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field login
# Get password value
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field password
# Get description
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field description
# Get URL
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field url
# Get tags (comma-separated)
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field tags

# Get a custom password field (e.g., API_KEY)
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --field text_field

# Generate TOTP code from shortcut
passwork-cli get --shortcut-id "68d6c94bec3a3fe41209546e" --totp-code "totp_secret"
```

## How it works

1. Passwork CLI connects to your Passwork server using the provided credentials
2. It retrieves the item or shortcut by ID
3. The item is decrypted using your master key
4. If `--totp-code` is specified, a TOTP code is generated from the specified field and printed
5. If `--field` is specified, only that field's value is printed
6. If neither `--totp-code` nor `--field` is specified, the password value is printed (or an error if empty)

## Using in scripts

The `get` command is perfect for automation scripts where you need to retrieve password values:

```bash
#!/bin/bash
DB_PASSWORD=$(passwork-cli get \
  --password-id "db_prod_password")

echo "Connecting to database..."
mysql -u admin -p"$DB_PASSWORD" mydatabase
```

## Using environment variables

You can set Passwork credentials as environment variables to simplify commands:

```bash
export PASSWORK_HOST="https://passwork.example.com"
export PASSWORK_TOKEN="your_access_token"
export PASSWORK_MASTER_KEY="your_master_key"

# Then get without specifying credentials
passwork-cli get --password-id "68793e13dfc88d879e0f2e39"
```

If needed, you can also pass a refresh token:

```bash
export PASSWORK_REFRESH_TOKEN="your_refresh_token"
```

This is particularly useful for automation scripts and CI/CD pipelines where credentials can be securely stored as environment variables.
