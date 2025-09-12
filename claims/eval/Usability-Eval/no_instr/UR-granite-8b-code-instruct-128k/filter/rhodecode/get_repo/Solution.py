from rhodecode import RhodeCode

# Create a RhodeCode object
rc = RhodeCode()

# Get a repository by name or repository_id
repository = rc.get_repository(name='my_repository')

# Get the members associated with the repository
members = repository.get_members()

# Print the members
for member in members:
    print(member)
