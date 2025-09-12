# Import necessary module from rhodecode
from rhodecode import fetch_repos
from rhodecode.model import Repository, UserGroup, User

def get_repository_members(repo_identifier):
    """
    Get the repository object and its associated user groups and users based on repository name or ID.

    :param repo_identifier: Repository name or ID to search
    :return: Dictionary containing repository name and its associated user groups and users
    """
    try:
        # Fetch repository based on name or id
        repo = Repository.get_repo_by_name_or_id(repo_identifier)
        
        if repo is None:
            raise ValueError("Repository not found")
        
        # Fetching user groups and users associated with the repository
        user_groups = repo.user_groups  # Assuming repo.user_groups gives associated user groups
        users = repo.users  # Assuming repo.users gives associated users

        # Prepare the output dictionary
        output = {
            'repository_name': repo.name,
            'user_groups': [group.name for group in user_groups],
            'users': [user.username for user in users]
        }
        
        return output

    except Exception as e:
        return {"error": str(e)}

# Example usage:
# result = get_repository_members("sample-repo")
# print(result)
