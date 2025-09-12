
import rhodecode

# Initialize RhodeCode client
rc = rhodecode.Client('http://your-rhodecode-server:8000')

# Set the repository to update
repo_name = 'your-repository'

# Define the new data to be updated
new_data = {
    'description': 'New description',
    'permissions': [
        {'username': 'john', 'role': 'developer'},
        {'username': 'mary', 'role': 'collaborator'}
    ]
}

# Update the repository with the new data
rc.update_repository(repo_name, new_data)
