---
name: planka
description: Use when managing Planka boards, projects, and cards.
category: productivity
---

# Planka Skill

This skill provides a Python CLI client to interact with **Planka** boards via its REST API. You can use it to fetch projects, create cards, update lists, and automate Kanban tasks.

## Environment Setup
Set `PLANKA_BASE_URL` (e.g. `https://planka.domain.com`), and either `PLANKA_EMAIL` + `PLANKA_PASSWORD` or `PLANKA_TOKEN`.

## Using the Script
The client is located at `scripts/planka_client.py`. Run it via python3:

1. **List all Projects:** `get-projects`
2. **List Boards in Project:** `get-boards <project_id>`
3. **List Lists in Board:** `get-lists <board_id>`
4. **List Cards in List:** `get-cards <list_id>`
5. **Create Card:** `create-card <list_id> "<card_name>"`

## Workflow
If the user asks to manage Planka:
1. Make sure credentials are set in the environment or ask the user.
2. Call the script to find IDs and perform actions.

(Note: You can read the script source if you want to extend it, it uses standard `urllib`.)