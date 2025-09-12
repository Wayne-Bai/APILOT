from rhodecode.repository.metadata import Repository

def get_repository(repository_name_or_id):
    """
    Function to get an existing repository by name or repository_id.
    """
    # Instantiate a Repository object
    repository = Repository(Repository.get(repository_name_or_id))

    # Check if the repository exists
    if repository is None:
        return "Repository not found."

    # Return users, groups, or users associated with that repository
    return repository.members

# Test the function
repository_name_or_id = "my_repository"
get_repository(repository_name_or_id)
