from rhodecode import Repository, User, Group

def get_repository_members(repository_name_or_id):
    # Get the repository by name or ID
    repo = Repository.get_by_name_or_id(repository_name_or_id)

    # Get all users associated with the repository
    users = [user.username for user in repo.users]

    # Get all groups associated with the repository
    groups = [group.name for group in repo.groups]

    # Combine users and groups into a single list
    members = users + groups

    return members
