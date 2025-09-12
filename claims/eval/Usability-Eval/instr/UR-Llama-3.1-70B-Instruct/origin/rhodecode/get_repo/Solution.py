from rhodecode.model.db import Session
from rhodecode.model.repo import Repository
from rhodecode.model.repo_group import RepoGroup
from rhodecode.model.user import User, users_group_map
from rhodecode.model.users_group import UsersGroup

def get_repository_by_name(repo_name):
    """
    Retrieves a repository by its name.
    
    Parameters:
    repo_name (str): The name of the repository.
    
    Returns:
    Repository: The retrieved repository.
    """
    return Repository.query().filter(Repository.repo_name == repo_name).first()

def get_repository_by_id(repo_id):
    """
    Retrieves a repository by its ID.
    
    Parameters:
    repo_id (int): The ID of the repository.
    
    Returns:
    Repository: The retrieved repository.
    """
    return Repository.query().get(repo_id)

def get_repository_members(repo):
    """
    Retrieves the members of a repository.
    
    Parameters:
    repo (Repository): The repository to get the members for.
    
    Returns:
    dict: A dictionary containing the users and groups associated with the repository.
    """
    members = {'users': [], 'groups': []}
    repo_group_ids = [rg.repo_group_id for rg in RepoGroup.query().filter(RepoGroup.repo_id == repo.repo_id).all()]
    users = User.query().join(users_group_map).filter(users_group_map.c.group_id.in_(repo_group_ids)).all()
    groups = UsersGroup.query().join(users_group_map).filter(users_group_map.c.group_id.in_(repo_group_ids)).all()

    members['users'] = [{'username': user.username, 'name': user.name} for user in users]
    members['groups'] = [{'group_name': group.users_group_name, 'group_id': group.users_group_id} for group in groups]

    return members

# Usage
if __name__ == '__main__':
    repo_name ='my-repo'
    repo = get_repository_by_name(repo_name)
    
    if repo:
        members = get_repository_members(repo)
        print(f'Members of repository {repo_name}:')
        print(members)
    else:
        print(f'Repository {repo_name} not found.')
