# Import the RhodeCode API client library
import rhodecode.api

# Initialize the RhodeCode API client
def update_repository(repo_name, new_name, new_description, username, password, api_url, new_owner=None, new_groups=None):
    # Create a RhodeCode API client instance
    rc = rhodecode.api.Client(url=api_url, username=username, password=password)

    # Get the repository by name
    repo = rc.repositories.get_by_name(repo_name)

    # Update the repository information
    repo.name = new_name
    repo.description = new_description

    # Update the repository if a new owner or groups are provided
    if new_owner:
        # Update the repository owner
        repo.owner = new_owner
    if new_groups:
        # Update the repository groups (assign/reassign permissions)
        rc.permissions.change_repo_group(repo, new_groups)

    # Save the changes
    repo.save()

    return repo

# Example usage:
repo_name = 'old-repo'
new_name = 'new-repo'
new_description = 'New repository description'
username = 'admin'
password = 'password123'
api_url = 'https://localhost:8000'
new_owner = 'john'
new_groups = ['read-only','read-write']

updated_repo = update_repository(repo_name, new_name, new_description, username, password, api_url, new_owner=new_owner, new_groups=new_groups)

print(updated_repo)
