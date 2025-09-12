
# Import the required modules
from rhodecode import RhodeCode

# Initialize the connection to RhodeCode server
rhodecode = RhodeCode('https://your-rhodecode-url.com', 'username', 'password')

# Define a function to get the repository by its name or repository_id
def get_repository_members(repository_name):
    repo = rhodecode.get_repository(repository_name)
    
    if repo:
        # Get the users or groups associated with the repository
        members = rhodecode.get_repository_members(repository=repo)
        
        return members
    else:
        return "Repository not found"

# Call the function with the repository name or repository_id
repository_members = get_repository_members('repository_name')

# Print the output
print(repository_members)
