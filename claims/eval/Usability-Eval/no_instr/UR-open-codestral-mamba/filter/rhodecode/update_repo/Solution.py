from rhodecode.repositories import RepositoryManager

# Instantiate the RepositoryManager
rm = RepositoryManager()

# Define the repository information
repo_name = 'YourRepositoryName'
repo_path = '/path/to/your/repository'

# Update the repository
repo = rm.update_repository(repo_name, repo_path)

# Check if the repository was updated
if repo:
    print(f'Successfully updated repository {repo_name}')
else:
    print(f'Failed to update repository {repo_name}')
