import json
from rhodecode.model.repo import RepoModel

def update_repository(repo_name, repo_description, repo_type):
    """
    Updates a repository with the given information.

    :param repo_name: The name of the repository to update.
    :param repo_description: The new description for the repository.
    :param repo_type: The type of the repository (e.g. 'git', 'hg','svn').

    :return: True if the repository was updated successfully, False otherwise.
    """

    # Create a connection to the RhodeCode database
    db_session = RepoModel.get_db_session()

    try:
        # Get the repository to update from the database
        repo = RepoModel.get_repo(repo_name, db_session)

        # Check if the repository exists
        if repo is None:
            print("Repository not found.")
            return False

        # Update the repository description and type
        repo.repo_description = repo_description
        repo.repo_type = repo_type

        # Save the changes to the database
        db_session.commit()

        return True

    except Exception as e:
        # Handle any database errors
        print(f"Error updating repository: {str(e)}")
        return False

    finally:
        # Close the database session
        db_session.close()

# Example usage
repo_name = "my-repo"
repo_description = "This is my repository."
repo_type = "git"

if update_repository(repo_name, repo_description, repo_type):
    print(f"Repository '{repo_name}' updated successfully.")
else:
    print(f"Failed to update repository '{repo_name}'.")
