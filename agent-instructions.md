# Planka Integration Instructions for AI Agents

Copy this text into your system prompt, `.clinerules`, or custom instructions so that your AI assistant (Claude, Cline, RooCode, Cursor, etc.) knows how to interact with your Planka boards.

---

## Tool: Planka Kanban API
You have access to a local CLI script (`planka_client.py`) that manages Planka Kanban boards. Use this script to read the user's boards, find lists, create cards, and orchestrate project management automatically.

### Requirements:
Ensure the environment running this script has Python 3 installed. The script depends only on standard Python libraries.

### Command Reference:
Run the script using `python planka_client.py <action> [args...]`.

**Available Actions:**
1. `get-projects`
   - Returns: List of all projects and their IDs.
2. `get-boards <project_id>`
   - Returns: List of boards for the specified project.
3. `get-lists <board_id>`
   - Returns: List of all lists (columns) inside a board.
4. `get-cards <list_id>`
   - Returns: All cards inside a specific list.
5. `create-card <list_id> "<card_name>" ["optional_description"]`
   - Action: Creates a new card in the specified list.
6. `assign-card <card_id> <user_id>`
   - Action: Assigns a user to a specific card.
7. `create-project "<project_name>"`
   - Action: Creates a new private project.
8. `create-board <project_id> "<board_name>"`
   - Action: Creates a new board in the given project.

### Workflow Example:
When asked to create a task in Planka:
1. Run `python planka_client.py get-projects` to find the correct project ID.
2. Run `python planka_client.py get-boards <project_id>` to find the right board.
3. Run `python planka_client.py get-lists <board_id>` to find the "To Do" or corresponding list ID.
4. Run `python planka_client.py create-card <list_id> "Task Title" "Task Description"`.
