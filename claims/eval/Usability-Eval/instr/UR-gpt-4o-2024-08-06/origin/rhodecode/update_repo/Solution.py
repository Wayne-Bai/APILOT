from rhodecode.client import RhodeCodeClient

# Create a client instance
client = RhodeCodeClient('http://your-rhodecode-instance-url', 'your-api-key')

# Define the repository name and new details you want to update
repo_name = 'your-repo-name'
update_data = {
    'description': 'Updated repository description',
    'contact': 'new_contact@example.com',
    'private': False  # Example to change the repository's privacy setting
}

try:
    # Update the repository
    response = client.call_api('update_repo_v2', repo_name=repo_name, repo_data=update_data)
    
    if response.get('status') == 'success':
        print("Repository updated successfully.")
    else:
        print("Failed to update the repository:", response.get('error'))
except Exception as e:
    print("An error occurred:", str(e))
