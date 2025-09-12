import requests

# URL of the RhodeCode server
rhodecode_url = "https://your-rhodecode-instance.com/api"

# Authentication
auth_token = "your-auth-token"
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json"
}

# Repository data to update
repo_name = "example-repo"
new_repo_data = {
    "description": "Updated repository description",
    "settings": {
        "default_branch": "main",
        # Add other settings you want to update
    }
}

# API endpoint to update a repository
update_repo_endpoint = f"{rhodecode_url}/repo/{repo_name}"

# Make a request to update the repository
response = requests.patch(update_repo_endpoint, json=new_repo_data, headers=headers)

# Check response
if response.status_code == 200:
    print("Repository updated successfully.")
else:
    print(f"Failed to update repository: {response.status_code} {response.text}")
