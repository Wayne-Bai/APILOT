import rhodecode

def update_repository(repo_id, update_info):
    try:
        repo = rhodecode.Repository(repo_id)
        repo.update(update_info)
        print(f"Repository {repo_id} updated successfully.")
    except Exception as e:
        print(f"Failed to update repository {repo_id}: {e}")

# Example usage
repo_id = 'your_repository_id'
update_info = {
    'description': 'New repository description',
    'name': 'New repository name',
    # Add other update information as needed
}

update_repository(repo_id, update_info)
