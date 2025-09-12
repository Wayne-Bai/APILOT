from rhodecode.model.db import Session
from rhodecode.model.repo import Repository
from rhodecode.model.repo_group import RepoGroup
from rhodecode.model.auth import User, HGGroup

def get_repository(repo_name_or_id):
    repo = Repository.get_by_repo_name(repo_name_or_id) or Repository.get_by_repo_id(repo_name_or_id)
    if not repo:
        raise Exception("Repository not found")

    # Get members (users and groups) associated with the repository
    members = Session().query(User, HGGroup).\
        outerjoin(HGGroup.user_user_group_table).\
        filter(HGGroup.repo_group_to_group==repo.repo_group_id).\
        all()

    result = {
       'repository': {
            'name': repo.repo_name,
            'id': repo.repo_id,
        },
       'members': [],
    }

    for member in members:
        user = member[0]
        group = member[1]
        if user:
            result['members'].append({
                'type': 'user',
                'username': user.username,
                'name': user.name,
                'email': user.email,
            })
        if group:
            result['members'].append({
                'type': 'group',
                'group_name': group.users_group_name,
                'group_description': group.users_group_description,
            })

    return result

# Usage
repo_name_or_id ='my_repo'
print(get_repository(repo_name_or_id))
