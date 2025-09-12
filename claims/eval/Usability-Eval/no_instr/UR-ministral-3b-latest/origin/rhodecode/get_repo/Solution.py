from rhodecode_client import RhodeCodeClient

# Create a RhodeCodeClient instance with your API credentials
client = RhodeCodeClient("hostname", "username", "api_key")

# Get the repository
repo = client.repository.get("repository_name" or repository_id)

# Get the members for the repository
members = repo.members

# Print the users, groups, or users associated with that repository
for member in members:
    print(member)
