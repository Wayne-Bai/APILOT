import rhodecode

# Define the connection parameters
url = "https://your.rhodecode.server"
username = "your_username"
password = "your_password"

# Create a connection to the RhodeCode server
rc = rhodecode.RhodeCode(url, username, password)

def get_repository_members(repo_identifier):
    # Get the repository details
    repo = rc.get_repository(repo_identifier)
    
    # Retrieve the members associated with the repository
    members = repo.get_members()  # This may vary based on the actual library functionality

    return members

# Example usage
repo_name_or_id = "your_repository_name_or_id"
members = get_repository_members(repo_name_or_id)
print(members)
