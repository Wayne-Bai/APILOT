import rhodecode

def get_repository(repo_name_or_id):
    repo = rhodecode.get_repository(repo_name_or_id)
    users_groups = repo.get_users_groups()
    return users_groups
