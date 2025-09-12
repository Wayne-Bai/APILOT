
import rhodecode

# Connect to the RhodeCode instance
client = rhodecode.connect("https://your-rhodecode-instance.com", "your_username", "your_password")

# Update a repository with the given information
repository = client.repository("repository_name")
repository.update(description="New description", is_private=True)

print("Repository updated successfully")
