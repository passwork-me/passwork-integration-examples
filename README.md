# Passwork API Integration Examples

This repository contains practical examples for working with the Passwork API using approaches:

- DevOps/CI workflows via `passwork-cli` (retrieving secrets, searching by tags/folders, direct API calls)
- Programmatic integrations via the Python connector (create/read/update/delete objects, sessions, shortcuts, snapshots, etc.)

This repository does not contain the sources of the CLI or the connector — only usage examples.

## Install the Python Connector

Requires Python 3.10+.

```bash
pip install git+ssh://git@github.com:passwork-me/passwork-python.git
or
pip install git+https://github.com/passwork-me/passwork-python.git
```

## Repository Structure

- `python/` — examples that use the Python connector to interact with Passwork.
  - Includes examples for: creating company vaults and vaults (`create_company_vault.md`, `create_private_vault.md`),
    CRUD for items (`create_item.md`, `get_item.md`, `get_items.md`, `update_item.md`, `delete_item.md`),
    search (`search_item.md`, `search_shortcut.md`), shortcuts (`create_shortcut.md`, `get_shortcut.md`), snapshots (`get_snapshot.md`),
    sessions and tokens (`session.md`, `refresh_token.md`), direct calls (`general_call.md`), user and links (`create_user.md`, `create_link.md`),
    inbox and SSL options (`get_inbox_item.md`, `no_ssl_verify.md`), vault retrieval (`get_vault.md`).

- `cli/` — copy‑ready recipes for DevOps/CI pipelines using `passwork-cli`.
  - Open the corresponding files for scenarios:
    - `single_password.md` — fetch a single secret
    - `multiple_passwords.md` — fetch multiple secrets
    - `search_by_tags.md` — search by tags
    - `folder_search.md` — search in a folder
    - `custom_fields.md` — work with custom fields
    - `refresh_token.md` — refresh tokens
    - `direct_api_call.md` — direct API calls
    - `cmd_parameter.md` — pass secrets as command parameters
    - `get.md` — get items and shortcuts, extract specific fields, generate TOTP codes
    - `update.md` — update data items

- `pipelines/` — CI example using `passwork-cli` in a pipeline environment.
  - `pipeline.yml` demonstrates:
    - retrieving database credentials to run migrations
    - retrieving API/deploy keys to run deployment scripts
    - sending a notification via a direct API call
  - Uses the Docker image `passwork-cli:latest` as the build image.

## Official Documentation

- API overview: [API and integrations — intro](https://passwork.pro/tech-guides/api-and-integrations/intro/)
- Python connector: [Python connector](https://passwork.pro/tech-guides/api-and-integrations/python-connector/)
- CLI utility: [CLI utility](https://passwork.pro/tech-guides/api-and-integrations/cli-utility/)
- Docker image for CLI: [Docker container for CLI](https://passwork.pro/tech-guides/api-and-integrations/docker-container-for-cli/)
- Source code (Python connector and CLI): [passwork-me/passwork-python](https://github.com/passwork-me/passwork-python)

## License

MIT — see `LICENSE`.
