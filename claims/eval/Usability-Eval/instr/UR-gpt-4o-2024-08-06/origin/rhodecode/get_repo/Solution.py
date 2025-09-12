from rhodecode import api

def get_repository_members(rc_url, rc_api_key, repo_identifier):
    """
    Get users or groups associated with a repository in RhodeCode.

    :param rc_url: Rhodecode instance URL
    :param rc_api_key: API Key for authentication
    :param repo_identifier: Name or ID of the repository
    :return: Dictionary containing associated users and groups
    """
    client = api.Client(rc_url, api_key=rc_api_key)

    # Get repository information
    repo_info = client.get_repo(repo_identifier)

    if not repo_info:
        raise ValueError("Repository not found.")

    # Get repository permissions
    repo_permissions = client.get_repo_permissions(repo_identifier)

    members = {
        'user_permissions': [],
        'group_permissions': [],
    }

    for perm in repo_permissions:
        if perm['type'] == 'user':
            members['user_permissions'].append({
                'username': perm['username'],
                'permissions': perm['permissions']
            })
        elif perm['type'] == 'group':
            members['group_permissions'].append({
                'group_name': perm['group_name'],
                'permissions': perm['permissions']
            })

    return members

# Usage example (assuming proper URL and API key are provided):
# rc_url = 'http://rhodecode.example.com/api'
# rc_api_key = 'your_api_key'
# repo_name_or_id = 'my-repo'
# members = get_repository_members(rc_url, rc_api_key, repo_name_or_id)
# print(members)
