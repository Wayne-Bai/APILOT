from rhodecode.rhodecode import RhodecodeClient

# Setting up Rhodecode client
client = RhodecodeClient('your_username', 'your_password', server_url='your_server_url')

# Retrieving a repository by name
repo = client.get_repository('your_repository_name')

# Updating repository information
updated_at = repo.data['updated_at']
new_updated_at = '2023-10-15T10:00:00Z'

# Patching the updated_at field with the new value
repo.data['updated_at'] = new_updated_at

# Committing changes
updated_repo = client.update_repository(repo.id, repo.data)

print(f"Updated repository: {updated_repo}")
