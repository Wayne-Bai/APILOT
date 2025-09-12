from rhodecode.model.repo import RepoModel
from rhodecode.model.db import Session
from rhodecode.model.user import UserModel
from rhodecode.model.scm import ScmModel

# Assuming that we have a repo_name. Replace it with the actual repository name.
repo_name = 'existing-repo-name'

def get_repository_members(repo_name):
    session = Session()
    repo = session.query(RepoModel).filter(RepoModel.repo_name==repo_name).first()

    if repo:
        users = session.query(UserModel).filter(UserModel.user_id.in_(repo.users_group_ids)).all()
        groups = session.query(ScmModel).filter(ScmModel.users_group_id.in_(repo.users_group_ids)).all()

        return {"users": [user.username for user in users],
                "groups": [group.users_group_name for group in groups]}
    else:
        return "Repository not found"

print(get_repository_members(repo_name))
