# Planka AI Integration Client

This repository provides a universal Python CLI client that allows autonomous AI agents to interact with **Planka** (the open-source Kanban board). It can be used by Hermes Agent, **Cline**, **Claude Code**, **RooCode**, **Cursor**, and more.

## Installation & Setup

1. Clone or download this repository.
2. Set the following environment variables in your terminal, `.env` file, or global agent configuration:
   - `PLANKA_BASE_URL`: Base URL of your Planka instance (default: `http://localhost:3000`)
   - `PLANKA_EMAIL`: Your Planka login email
   - `PLANKA_PASSWORD`: Your Planka login password
   - `PLANKA_TOKEN`: Alternatively, use a direct access token

## Usage for Any AI Agent (Cline, Claude Code, RooCode)

To allow any terminal-based AI assistant to manage your Planka boards, simply provide them with the instruction set in `agent-instructions.md`.

For example, in **Cline** or **RooCode**:
1. Copy the contents of `agent-instructions.md` into your `.clinerules` file in the root of your workspace.
2. Ensure `scripts/planka_client.py` is in the directory or update the path in `.clinerules` accordingly.

In **Claude Code**:
You can add the instructions from `agent-instructions.md` to your prompt, or ask Claude Code to read `agent-instructions.md` before executing tasks.

## Usage for Hermes Agent

If you are using Hermes Agent:
1. Copy the contents of this repository to your Hermes skills directory (e.g. `~/.hermes/skills/productivity/planka`).
2. Hermes will automatically learn to use the tool via the provided `SKILL.md`.

## Available Script Actions

The `planka_client.py` relies solely on standard Python libraries (no `pip install` needed). 
Run it with: `python scripts/planka_client.py <action> [args]`

- `get-projects`
- `get-boards [project_id]`
- `get-lists <board_id>`
- `get-cards <list_id>`
- `create-card <list_id> "<card_name>" [description]`
- `assign-card <card_id> <user_id>`
- `create-project "<project_name>"`
- `create-board <project_id> "<board_name>"`
