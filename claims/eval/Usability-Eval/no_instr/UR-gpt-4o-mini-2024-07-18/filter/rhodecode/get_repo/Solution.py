import rhodecode

def get_repository_members(repository_id):
    # Create a connection to RhodeCode
    client = rhodecode.Client('http://your-rhodecode-instance.com', 'your_username', 'your_password')

    # Fetch the repository by its ID
    repository = client.get_repository(repository_id)

    # Get the members associated with the repository
    members = repository.get_members()

    return members

# Example usage
repository_id = 'your_repository_id'  # Replace with your actual repository ID
members = get_repository_members(repository_id)

# Output the members
for member in members:
    print(member)
