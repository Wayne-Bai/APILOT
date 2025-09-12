import rhodecode
from rhodecode.exceptions import NotFound

# Replace these with actual connection details
URL = 'http://your-rhodecode-server-url'
USERNAME = 'your-username'
PASSWORD = 'your-password'

# Initialize the Rhodes code client
client = rhodecode.RhodeCode(URL, USERNAME, PASSWORD)

# Function to get the repository by name or ID
def get_repository(repository_name=None, repository_id=None):
    if repository_name:
        try:
            repo = client.get_repository_by('name', repository_name)
        except NotFound:
            return f"Repository with name {repository_name} not found."
    elif repository_id:
        try:
            repo = client.get_repository_by('id', repository_id)
        except NotFound:
            return f"Repository with ID {repository_id} not found."
    else:
        return "Repository name or ID is required."

    return repo

# Function to get the members of the repository
def get_repository_members(repo):
    members = repo.repository_members()
    return members

# Replace this with the actual repository name or ID
repository_name = 'your_repository_name'
# repository_id = 'your_repository_id'  # Uncomment this line if using repository_id
# repository_name = None
# repository_id = 'your_repository_id'  # Comment this line if using repository_name

repo = get_repository(repository_name=repository_name)  # Change the function call to use repository_id if needed
if isinstance(repo, dict):
    repo_name = repo.get('name')
    repo_id = repo.get('id')
    if repo_name:
        print(f"Repository found: {repo_name} with ID: {repo_id}")
    else:
        print(repo)

    # Fetching members of the repository
    repo_members = get_repository_members(repo)
    print("Members associated with the repository:")
    for member in repo_members:
        print(member)
