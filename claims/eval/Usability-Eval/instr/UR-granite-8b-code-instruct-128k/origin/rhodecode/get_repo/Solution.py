
import rhodecode

def get_repository_members(repo_name_or_id):
    # Create a RhodeCode API client
    client = rhodecode. APIClient()

    # Get the repository
    repo = client.repositories.get(repo_name_or_id)

    # Get the members associated with the repository
    members = repo.members

    return members
