from rhodecode import RhodeCode

def update_repository(repo_id, repo_name, repo_description, repo_public):
    # Initialize RhodeCode client
    rc = RhodeCode('https://your-rhodecode-instance.com', 'username', 'password')

    # Update repository
    rc.repos.update(repo_id, name=repo_name, description=repo_description, public=repo_public)

    print(f"Repository {repo_name} updated successfully.")

# Replace 'repo_id', 'repo_name', 'repo_description', and 'repo_public' with the appropriate values
update_repository('repo_id', 'repo_name', 'repo_description', True)
