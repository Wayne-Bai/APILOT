
from rhodecode import RepositoryService

# Create an instance of the RepositoryService class
rhodecode = RepositoryService()

# Set the repository's URL and access token
repository_url = "https://git.example.com/my-repo"
access_token = "your-access-token"

# Update the repository with the given information
rhodecode.update_repository(
    url=repository_url,
    access_token=access_token,
    name="My Updated Repository",
    description="This is an updated repository.",
    is_private=True,
)
