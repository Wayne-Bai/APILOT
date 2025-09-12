import rhodecode

def update_repository(repo_name, description, license_type):
    # Authenticate with RhodeCode
    client = rhodecode.Client('username', 'password')

    # Get the repository
    repo = client.get_repository(repo_name)

    # Update the repository information
    repo.description = description
    repo.license_type = license_type

    # Save the changes
    repo.save()

    return 'Repository updated successfully!'
