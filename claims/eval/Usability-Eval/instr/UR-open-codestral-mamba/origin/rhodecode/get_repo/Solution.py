import rhodecode.api as rc

def get_repository_members(repository_name_or_id):
    # Get the repository object
    repository = rc.get_repository(repository_name_or_id)

    # Get the users, groups, and users associated with the repository
    users = repository.get_user_permissions()
    groups = repository.get_group_permissions()
    members = repository.get_members()

    # Return the members
    return users, groups, members

repository_name_or_id = 'my_repository'
users, groups, members = get_repository_members(repository_name_or_id)
print(f"Users: {users}")
print(f"Groups: {groups}")
print(f"Members: {members}")
