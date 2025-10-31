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
  - Includes examples for: creating company vaults and vaults (`create_company_vault.py`, `create_vault.py`),
    CRUD for items (`create_item.py`, `get_item.py`, `get_items.py`, `update_item.py`, `delete_item.py`),
    search (`search_item.py`), shortcuts (`create_shortcut.py`, `get_shortcut.py`), snapshots (`get_snapshot.py`),
    sessions and tokens (`session.py`, `refresh_token.py`), direct calls (`general_call.py`), user and links (`create_user.py`, `create_link.py`),
    inbox and SSL options (`get_inbox_item.py`, `get_item_no_ssl.py`), vault retrieval (`get_vault.py`).

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

## Official Documentation

- API overview: [API and integrations — intro](https://passwork.pro/tech-guides/api-and-integrations/intro/)
- Python connector: [Python connector](https://passwork.pro/tech-guides/api-and-integrations/python-connector/)
- CLI utility: [CLI utility](https://passwork.pro/tech-guides/api-and-integrations/cli-utility/)
- Docker image for CLI: [Docker container for CLI](https://passwork.pro/tech-guides/api-and-integrations/docker-container-for-cli/)
- Source code (Python connector and CLI): [passwork-me/passwork-python](https://github.com/passwork-me/passwork-python)

## License

MIT — see `LICENSE`.
