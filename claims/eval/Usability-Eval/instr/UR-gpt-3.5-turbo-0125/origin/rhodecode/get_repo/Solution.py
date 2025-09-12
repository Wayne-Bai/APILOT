
# Import necessary modules
from rhodecode import RhodeCode

# Initialize RhodeCode instance
rc = RhodeCode()

# Specify the repository name or repository_id you want to retrieve
repository_name = 'your_repository_name_here'
repository_id = 'your_repository_id_here'

# Get the repository by its name
repository = rc.get_repository_by_name(repository_name)

# Get the repository by its repository_id
# repository = rc.get_repository(repository_id)

# Get the members section for the repository
members = repository.get_members()

# Print or access the users, groups associated with the repository
for member in members:
    if member.is_group:
        print(f'Group: {member.name}')
    else:
        print(f'User: {member.username}')
