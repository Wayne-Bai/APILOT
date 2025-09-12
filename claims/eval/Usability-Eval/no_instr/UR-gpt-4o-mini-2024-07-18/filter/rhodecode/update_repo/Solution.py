import rhodecode

def update_repository(repo_id, update_info):
    # Assuming rhodecode has a suitable object to handle repositories
    repository = rhodecode.get_repository(repo_id)
    
    if repository:
        # Update repository details
        repository.name = update_info.get("name", repository.name)
        repository.description = update_info.get("description", repository.description)
        repository.default_branch = update_info.get("default_branch", repository.default_branch)
        
        # Save the changes back to the repository
        repository.save()
        
        print("Repository updated successfully.")
    else:
        print("Repository not found.")

# Example usage
update_info = {
    "name": "New Repository Name",
    "description": "Updated repository description.",
    "default_branch": "main"
}
update_repository("your_repo_id", update_info)
