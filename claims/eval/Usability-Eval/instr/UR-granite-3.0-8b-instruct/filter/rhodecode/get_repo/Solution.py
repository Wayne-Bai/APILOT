from rhodecode import RhodeCode

# Initialize RhodeCode client
rc = RhodeCode('http://localhost:8000', 'username', 'password')

# Get repository by name or repository_id
repo = rc.get_repository('my_repository')

# Get members of the repository
members = repo.get_members()

# Print members
for member in members:
    print(member.username)
