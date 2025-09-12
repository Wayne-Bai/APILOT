from rhodecode.model.db import Repository
from rhodecode.model.meta import Session

def update_repository(repo_id, new_info):
    # Create a new DB session
    session = Session()

    # Query the repository by its id
    repository = session.query(Repository).filter(Repository.repo_id == repo_id).first()

    if repository:
        # Update the repository information
        for key, value in new_info.items():
            setattr(repository, key, value)

        # Commit the change
        session.commit()
        session.close()
        return "Repository updated successfully"
    else:
        session.close()
        return "Repository not found"
