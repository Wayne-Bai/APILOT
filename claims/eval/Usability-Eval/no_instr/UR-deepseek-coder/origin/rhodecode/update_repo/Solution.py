import rhodecode

def update_repository(repo_name, new_description, new_owner, new_private):
    # Get the repository object
    repo = rhodecode.get_repo(repo_name)
    
    # Update the repository information
    repo.description = new_description
    repo.owner = new_owner
    repo.private = new_private
    
    # Save the changes
    repo.save()

# Example usage
update_repository('my_repo', 'Updated description', 'new_owner', True)
