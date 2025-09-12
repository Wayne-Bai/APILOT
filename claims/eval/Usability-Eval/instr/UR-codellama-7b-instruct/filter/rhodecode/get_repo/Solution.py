
import rhodecode

# Get an existing repository by its name or repository_id
repository = rhodecode.get_repo(name='my-repo', repository_id=123)

# Get the members associated with the repository
members = repository.get_members()

# Print the users and groups in the members list
for member in members:
    print(member)
