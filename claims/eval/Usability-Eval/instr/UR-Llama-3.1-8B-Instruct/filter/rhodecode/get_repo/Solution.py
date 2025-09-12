# Import the required library
from rhodecode.api.config import Config

# Get the API endpoint URL, username, and password as environment variables
API_ENDPOINT_URL = os.environ.get('RHC_ENDPOINT_URL')
USERNAME = os.environ.get('RHC_USERNAME')
PASSWORD = os.environ.get('RHC_PASSWORD')

# Initialize the RhodeCode API
rcapi = Config(
    api_endpoint_url=API_ENDPOINT_URL,
    username=USERNAME,
    password=PASSWORD
)

def get_repository_by_name_or_id(repo_name_or_id, rcapi, repo_id=None):
    """
    Gets an existing repository by its name or repository_id.

    Args:
        repo_name_or_id (str): The name or id of the repository.
        repo_id (str, optional): The id of the repository. Defaults to None.
        rcapi (Config): The RhodeCode API configuration.

    Returns:
        dict: The repository details.
    """

    # If repo_id is provided, use it to get the repository
    if repo_id:
        repo = rcapi.repository.get_by_id(repo_id)
    else:
        # If repo_name_or_id is not an integer, assume it's a name and search for the repository
        if not repo_name_or_id.isnumeric():
            repo = rcapi.repository.search_by_name(repo_name_or_id)
        # If repo_name_or_id is an integer, assume it's an id and get the repository
        else:
            repo = rcapi.repository.get_by_id(repo_name_or_id)

    # If the repository is not found, return None
    if not repo:
        return None

    # Get the members of the repository
    members = repo.get_members()

    # Print the repository details and its members
    print(f"Repository Name: {repo.name}")
    print(f"Repository ID: {repo.id}")
    print(f"Members:")
    for member in members:
        if isinstance(member, dict):
            print(f"  * {member['name']} ({member['username']})")
        else:
            print(f"  * {member.name} ({member.username})")

# Usage
repo_name_or_id = "myrepository"
repo_id = 123  # Replace with the actual repository id
get_repository_by_name_or_id(repo_name_or_id, rcapi, repo_id=repo_id)
