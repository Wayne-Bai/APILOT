from rhodecode.model.db import Repository, UserRepoToPerm, UserGroupRepoToPerm

def get_repository_with_members(repo_name_or_id):
    # Fetch the repository by its name or ID
    repository = Repository.get_by_repo_name_or_id(repo_name_or_id)
    
    if not repository:
        raise ValueError(f"Repository with name or ID '{repo_name_or_id}' not found.")
    
    # Fetch users and groups associated with the repository
    user_permissions = UserRepoToPerm.query() \
        .filter(UserRepoToPerm.repository == repository) \
        .all()
    
    group_permissions = UserGroupRepoToPerm.query() \
        .filter(UserGroupRepoToPerm.repository == repository) \
        .all()
    
    # Extract users and groups from the permissions
    users = [perm.user for perm in user_permissions]
    groups = [perm.group for perm in group_permissions]
    
    return {
        'repository': repository,
        'users': users,
        'groups': groups
    }

# Example usage:
# repo_info = get_repository_with_members('repo_name_or_id')
# print(repo_info)
