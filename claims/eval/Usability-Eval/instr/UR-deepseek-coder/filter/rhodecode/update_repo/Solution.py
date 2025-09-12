import rhodecode

def update_repository(repo_name, new_description, new_clone_url):
    # Fetch the repository by name
    repo = rhodecode.get_repo(repo_name)
    
    if repo:
        # Update the repository information
        repo.description = new_description
        repo.clone_url = new_clone_url
        
        # Save the updated repository information
        repo.save()
        print(f"Repository '{repo_name}' updated successfully.")
    else:
        print(f"Repository '{repo_name}' not found.")

# Example usage
update_repository('my_repo', 'Updated description', 'https://new-clone-url.com')
