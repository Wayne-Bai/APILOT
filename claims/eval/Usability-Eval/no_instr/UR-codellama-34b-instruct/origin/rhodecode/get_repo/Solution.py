
import rhodecode

# Initialize RhodeCode client
client = rhodecode.RhodeCodeClient()

# Set up authentication credentials
username = "your_username"
password = "your_password"
client.set_credentials(username, password)

# Get the repository by name or ID
repository = client.get_repository("my_repo")

# Print the repository's members section
print(repository.members)
