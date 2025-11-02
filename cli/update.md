# Updating Items and Shortcuts

This example demonstrates how to update items and shortcuts in Passwork using the `update` command. You can update individual fields or perform bulk updates with multiple fields at once.

## Use Cases

1. **Update single fields** - Change password, name, login, URL, description, tags, or custom fields individually
2. **Clear field values** - Set fields to empty by passing an empty string
3. **Bulk updates** - Update multiple fields in a single command
4. **Update custom fields** - Modify or add custom fields to items and shortcuts

## Basic Usage

You must specify either `--password-id` or `--shortcut-id` to identify which item to update.

```bash
passwork-cli update \
  --host "https://passwork.example.com" \
  --token "your_access_token" \
  --master-key "your_master_key" \
  --password-id "68793e13dfc88d879e0f2e39" \
  --password "new-password-value"
```

## Updating Standard Fields

You can update standard fields like password, name, login, URL, description, and tags:

```bash
# Update password
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --password "new-password"

# Update login
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --login "new-login"

# Update name
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --name "New Item Name"

# Update URL
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --url "https://example.com"

# Update description
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --description "Updated description"

# Update tags (comma-separated)
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --tags "tag1,tag2,tag3"

# Clear a field (set to empty)
passwork-cli update --password-id "68793e13dfc88d879e0f2e39" --description ""
```

## Updating Custom Fields

Custom fields are updated using the `--custom-*` syntax, where `*` is the name of your custom field:

```bash
# Update custom field API_KEY
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --custom-API_KEY "new-api-key-value"

# Update custom field with different name
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --custom-Database_Host "db.example.com"

# Clear custom field
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --custom-API_KEY ""
```

## Bulk Updates

You can update multiple fields in a single command:

```bash
# Update login and password together
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --login "new-login" \
  --password "new-password"

# Update multiple fields including custom field
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --password "new-password" \
  --description "Updated description" \
  --tags "production,database,api" \
  --custom-API_KEY "new-api-key-value"

# Full update with all fields
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --name "FullUpdateTest" \
  --login "super-login" \
  --password "super-password" \
  --description "Complete update" \
  --tags "combo,all,fields" \
  --url "https://example.com" \
  --custom-API_KEY "api-key-value"
```

## Working with Shortcuts

Shortcuts can be updated using the same syntax with `--shortcut-id`:

```bash
# Update shortcut fields
passwork-cli update \
  --shortcut-id "68d6c94bec3a3fe41209546e" \
  --password "shortcut-password" \
  --login "shortcut-login"

# Update shortcut with multiple fields
passwork-cli update \
  --shortcut-id "68d6c94bec3a3fe41209546e" \
  --name "ShortcutUpdate" \
  --description "Updated shortcut" \
  --tags "shortcut,updated" \
  --custom-API_KEY "shortcut-api-key"
```

## How It Works

1. Passwork CLI connects to your Passwork server using the provided credentials
2. It retrieves the item or shortcut by ID
3. The item is decrypted using your master key
4. The specified fields are updated with the new values
5. If a field is set to an empty string (`""`), that field will be cleared
6. Custom fields are updated or added using the `--custom-*` syntax
7. Tags can be specified as a comma-separated list, which will replace existing tags
8. The updated item is saved back to Passwork

## Important Notes

- **Name field**: Cannot be set to empty. If you try to set `--name ""`, an error will occur
- **Custom fields**: Use `--custom-FIELD_NAME` syntax where `FIELD_NAME` is the exact name of your custom field
- **Tags**: Provide tags as a comma-separated list (e.g., `"tag1,tag2,tag3"`). Empty string clears all tags
- **Empty values**: Passing an empty string (`""`) for any field will clear that field's value
- **Item type**: Use `--password-id` for items and `--shortcut-id` for shortcuts

## Using Environment Variables

You can set Passwork credentials as environment variables to simplify commands:

```bash
export PASSWORK_HOST="https://passwork.example.com"
export PASSWORK_TOKEN="your_access_token"
export PASSWORK_MASTER_KEY="your_master_key"

# Then update without specifying credentials
passwork-cli update \
  --password-id "68793e13dfc88d879e0f2e39" \
  --password "new-password"
```

This is particularly useful for automation scripts and CI/CD pipelines where credentials can be securely stored as environment variables.