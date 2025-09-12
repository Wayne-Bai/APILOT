
import rhodecode

# Get a specific repository by its name or ID
repo = rhodecode.get_repository(name='MyRepo')

# Get all users and groups associated with the repository
users_and_groups = repo.members()

# Print out the users and groups
for user in users_and_groups['users']:
    print(user['login'])

for group in users_and_groups['groups']:
    print(group['name'])
