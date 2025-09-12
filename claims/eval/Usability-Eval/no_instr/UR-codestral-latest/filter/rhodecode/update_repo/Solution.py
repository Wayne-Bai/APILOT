import requests
import json

# Replace these variables with your own Rhodecode server information
RHODECODE_URL = "https://rhodecode.example.com"
RHODECODE_API_TOKEN = "your_api_token"

def update_repository(repo_name, description):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'token {RHODECODE_API_TOKEN}',
    }

    data = {
        "repository": {
            "name": repo_name,
            "description": description,
        }
    }

    response = requests.post(f"{RHODECODE_URL}/api/repos", headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print(f"Repository {repo_name} created successfully.")
    elif response.status_code == 409:
        print(f"Repository {repo_name} already exists. Updating description...")
        response = requests.put(f"{RHODECODE_URL}/api/repos/{repo_name}", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print(f"Repository {repo_name} updated successfully.")
        else:
            print(f"Failed to update repository {repo_name}. Error: {response.text}")
    else:
        print(f"Failed to create repository {repo_name}. Error: {response.text}")

# Test the function
update_repository("my_repo", "This is my repository.")
