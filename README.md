# Hermes Agent Skill: Planka

This is a skill for **Hermes Agent** to interact with **Planka**, the open-source Kanban board.

It provides a Python CLI client to manage projects, boards, and cards via Planka's REST API, allowing the AI agent to automate Kanban workflows directly.

## Installation

1. Copy the contents of this repository to your Hermes skills directory (typically `~/.hermes/skills/productivity/planka`).
2. Make sure Python 3 is available in your agent's environment.

## Configuration

Set the following environment variables in your environment or Hermes context:

- `PLANKA_BASE_URL`: Base URL of your Planka instance (default: `http://localhost:3000`)
- `PLANKA_EMAIL`: Your Planka login email
- `PLANKA_PASSWORD`: Your Planka login password
- `PLANKA_TOKEN`: Alternatively, use a direct access token if available.

## Usage

The included script `scripts/planka_client.py` supports these actions:

- `get-projects`
- `get-boards [project_id]`
- `get-lists <board_id>`
- `get-cards <list_id>`
- `create-card <list_id> "<card_name>" [description]`
- `assign-card <card_id> <user_id>`
- `create-project "<project_name>"`
- `create-board <project_id> "<board_name>"`

*Note: For use by an autonomous AI agent, refer to `SKILL.md` for explicit workflow instructions.*
