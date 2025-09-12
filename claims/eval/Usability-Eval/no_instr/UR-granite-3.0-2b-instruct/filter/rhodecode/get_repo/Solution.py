from rhodecode import Repository, RepositoryMember

def get_repository_members(repository_name_or_id):
    # Create a Repository object
    repo = Repository(repository_name_or_id)

    # Get the repository
    repo_object = repo.get()

    # Get the members of the repository
    members = [member.username for member in repo_object.members]

    return members
