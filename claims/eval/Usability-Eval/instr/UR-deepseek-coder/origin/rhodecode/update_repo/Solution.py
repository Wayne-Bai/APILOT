import rhodecode

def update_repository(repo_name, new_description=None, new_owner=None, new_clone_uri=None):
    # Fetch the repository by name
    repo = rhodecode.get_repo(repo_name)
    
    if repo is None:
        raise ValueError(f"Repository '{repo_name}' not found.")
    
    # Update the repository description if provided
    if new_description is not None:
        repo.description = new_description
    
    # Update the repository owner if provided
    if new_owner is not None:
        repo.owner = new_owner
    
    # Update the repository clone URI if provided
    if new_clone_uri is not None:
        repo.clone_uri = new_clone_uri
    
    # Save the changes
    repo.save()
    
    print(f"Repository '{repo_name}' updated successfully.")

# Example usage
# update_repository('my_repo', new_description='Updated description', new_owner='new_owner', new_clone_uri='new_clone_uri')
