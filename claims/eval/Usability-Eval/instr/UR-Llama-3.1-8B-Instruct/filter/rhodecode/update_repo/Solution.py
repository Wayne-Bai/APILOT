# Import required modules
from RhodeCode import RhodeCode

# Create a RhodeCode instance with your API URL and credentials
api_url = "https://your-rhodecode-instance.com/api"
username = "your-username"
password = "your-password"

rc = RhodeCode(api_url, username, password)

# Create a new repository or get an existing one
repository_name = "your-repo-name"
repository_data = {
    "name": repository_name,
    "description": "Your repository description",
    "visibility": "public"  # Can be 'public', 'private', or 'internal'
}

# Update the repository
try:
    repository = rc.update_repo(repository_name, repository_data)
    print("Repository updated successfully")
    print("Repository ID:", repository['id'])
except Exception as e:
    print("Error updating repository:", str(e))
