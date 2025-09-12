from rhodecode import RhodeCode

# Initialize the RhodeCode client
rc = RhodeCode('http://localhost:8001', 'username', 'password')

# Get the repository by name or repository_id
repo = rc.get_repository('repo_name_or_id')

# Get the members of the repository
members = repo.get_members()

# Print the members
for member in members:
    print(member['name'])
