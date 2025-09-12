# Import the required library
from mercurial.api import changesets

# Import the RhodeCode API module
from rc_api import RhodeCodeAPI

# Initialize the RhodeCode API
api = RhodeCodeAPI('http://localhost:9980', 'admin', 'password')

# Replace'repo_name' or'repo_id' with actual repository name or ID
repo_id ='repo_name'  # or'repo_id' as an integer

# Function to get an existing repository
def get_repository(repo_id):
    try:
        repository = api.repositories.get(id=repo_id)
        return repository
    except Exception as e:
        print("An error occurred: ", e)

# Function to get repository members
def get_repository_members(repo_id):
    try:
        repository = api.repositories.get(id=repo_id)
        members = repository.members.all()
        return members
    except Exception as e:
        print("An error occurred: ", e)

# Get the repository and its members
repository = get_repository(repo_id)
members = get_repository_members(repo_id)

# Print the results
print("Repository Details:")
print("------------------")
print(f"Name: {repository.name}")
print(f"URL: {repository.url}")
print(f"ID: {repository.id}")

print("\nRepository Members:")
print("-------------------")
for member in members:
    print(f"Username: {member.username}")
    print(f"Role: {member.role}")
    print("-------------------")
