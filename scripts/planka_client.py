import urllib.request
import urllib.error
import urllib.parse
import json
import os
import sys

BASE_URL = os.environ.get('PLANKA_BASE_URL', 'http://localhost:3000').rstrip('/')
EMAIL = os.environ.get('PLANKA_EMAIL')
PASSWORD = os.environ.get('PLANKA_PASSWORD')
TOKEN = os.environ.get('PLANKA_TOKEN')

def request(method, path, data=None):
    global TOKEN
    url = f"{BASE_URL}{path}"
    headers = {'Content-Type': 'application/json'}
    
    if not TOKEN and EMAIL and PASSWORD and path != '/api/access-tokens':
        auth_data = json.dumps({'emailOrUsername': EMAIL, 'password': PASSWORD}).encode()
        try:
            req = urllib.request.Request(f"{BASE_URL}/api/access-tokens", data=auth_data, headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                resp = json.loads(response.read().decode())
                TOKEN = resp['item']
        except Exception as e:
            print(f"Auth error: {e}", file=sys.stderr)
            sys.exit(1)
            
    if TOKEN:
        headers['Authorization'] = f"Bearer {TOKEN}"
        
    encoded_data = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 204:
                return {}
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        print(f"HTTPError {e.code}: {err_msg}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python planka_client.py <action> [args...]")
        return
        
    action = sys.argv[1]
    
    if action == "get-projects":
        res = request('GET', '/api/projects')
        print(json.dumps(res, indent=2, ensure_ascii=False))
        
    elif action == "get-boards":
        res = request('GET', '/api/projects')
        for p in res.get('items', []):
            if not len(sys.argv) > 2 or str(p['id']) == sys.argv[2]:
                print(f"=== Project {p['name']} ({p['id']}) boards ===")
                boards = request('GET', f"/api/projects/{p['id']}")
                print(json.dumps(boards.get('included', {}).get('boards', []), indent=2, ensure_ascii=False))
                
    elif action == "get-lists":
        board_id = sys.argv[2]
        res = request('GET', f"/api/boards/{board_id}")
        print(json.dumps(res.get('included', {}).get('lists', []), indent=2, ensure_ascii=False))
        
    elif action == "get-cards":
        list_id = sys.argv[2]
        res = request('GET', f"/api/lists/{list_id}/cards")
        print(json.dumps(res.get('items', []), indent=2, ensure_ascii=False))
        
    elif action == "create-card":
        list_id = sys.argv[2]
        name = sys.argv[3]
        desc = sys.argv[4] if len(sys.argv) > 4 else None
        data = {"listId": list_id, "name": name, "type": "project", "position": 65535}
        if desc: data["description"] = desc
        res = request('POST', f"/api/lists/{list_id}/cards", data)
        print("Success:", json.dumps(res.get('item', {}), indent=2, ensure_ascii=False))

    elif action == "assign-card":
        card_id = sys.argv[2]
        user_id = sys.argv[3]
        res = request('POST', f"/api/cards/{card_id}/card-memberships", {"userId": user_id})
        print("Success:", json.dumps(res.get('item', {}), indent=2, ensure_ascii=False))

    elif action == "create-project":
        name = sys.argv[2]
        res = request('POST', '/api/projects', {"name": name, "type": "private"})
        print("Success:", json.dumps(res.get('item', {}), indent=2, ensure_ascii=False))

    elif action == "create-board":
        project_id = sys.argv[2]
        name = sys.argv[3]
        res = request('POST', f"/api/projects/{project_id}/boards", {"name": name, "position": 65535})
        print("Success:", json.dumps(res.get('item', {}), indent=2, ensure_ascii=False))
        
    else:
        print(f"Action '{action}' not recognized.")

if __name__ == "__main__":
    main()
