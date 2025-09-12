from rhodecode.model.db import Repository, UserRepoToPerm, UserGroupRepoToPerm

def get_repository_with_members(repo_name_or_id):
    # Fetch the repository by name or ID
    repository = Repository.get_by_repo_name(repo_name_or_id) or Repository.get(repo_name_or_id)
    
    if not repository:
        raise ValueError(f"Repository with name or ID '{repo_name_or_id}' not found.")
    
    # Fetch users associated with the repository
    user_perms = UserRepoToPerm.query() \
        .filter(UserRepoToPerm.repository == repository) \
        .all()
    
    users = [perm.user for perm in user_perms]
    
    # Fetch user groups associated with the repository
    user_group_perms = UserGroupRepoToPerm.query() \
        .filter(UserGroupRepoToPerm.repository == repository) \
        .all()
    
    user_groups = [perm.users_group for perm in user_group_perms]
    
    return {
        'repository': repository,
        'users': users,
        'user_groups': user_groups
    }

# Example usage:
# repo_info = get_repository_with_members('repo_name_or_id')
# print(repo_info)
