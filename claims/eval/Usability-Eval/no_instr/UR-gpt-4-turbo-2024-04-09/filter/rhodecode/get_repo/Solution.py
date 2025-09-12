from rhodecode_api_client import RhodeCode

def get_repository_members(repo_identifier):
    # Initialize the RhodeCode API client
    client = RhodeCode(api_key="your_api_key_here")

    # Get repository details by name or ID
    if isinstance(repo_identifier, int):
        repo_info = client.get_repository_by_id(repo_identifier)
    else:
        repo_info = client.get_repository_by_name(repo_identifier)

    # Check if repository was found
    if not repo_info:
        print("Repository not found")
        return

    # Assuming the API has a method to get members of a repository
    members = client.get_repository_members(repo_info['id'])

    # Print details about members
    print("Members associated with repository:", repo_info['name'])
    for member in members:
        print(f"- {member['name']} (Type: {member['type']})")

# Example usage
get_repository_members("example_repo_name")
get_repository_members(1234)
