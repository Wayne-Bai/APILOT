# Importing necessary modules
import rhodecode
from rhodecode import MetadataAPI, ApiError

# Initialize the rhodecode API client
rc = MetadataAPI("http://localhost:5000", "user@example.com", "password")

# Function to get repository details
def get_repository_info(repo_name_or_id):
    try:
        repo_info = rc.repository.get(repo_name_or_id)

        # Get members information
        members_info = rc.repository.get_members(repo_name_or_id)

        # Print out the repository information and members
        print(f"Repository Name: {repo_info['name']}")
        print(f"Repository ID: {repo_info['id']}")
        print(f"Description: {repo_info['description']}")
        print("\nMembers: ")
        for member in members_info['members']:
            print(f"- Group: {member['group']}")
            print(f"  - Users: {member['users']}")

    except ApiError as e:
        print(f"An error occurred: {e}")

# Example usage (either provide repository name or repository ID)
get_repository_info("repository_name_or_id")
