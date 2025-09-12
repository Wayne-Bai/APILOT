import rhodecode

def update_repository(repo_name, new_description, new_owner, new_visibility):
    # Fetch the repository by name
    repo = rhodecode.get_repo(repo_name)
    
    if repo:
        # Update the repository information
        repo.description = new_description
        repo.owner = new_owner
        repo.private = new_visibility == 'private'
        
        # Save the changes
        repo.save()
        print(f"Repository '{repo_name}' updated successfully.")
    else:
        print(f"Repository '{repo_name}' not found.")

# Example usage
update_repository('my_repo', 'Updated description', 'new_owner', 'private')
