import rhodecode

# Get an existing repository by its name or ID
repository_name = "my_repository"
try:
    repository = rhodecode.get_repository(repository_name)
except rhodecode.RepositoryNotFoundError:
    print("Repository not found.")
    return

# Get the members of the repository
members = repository.members()

# Print the users associated with the repository
print("Users associated with repository:")
for member in members:
    if isinstance(member, rhodecode.User):
        print(f"- {member.username} ({member.email})")
