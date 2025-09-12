# Import the required libraries
from rhodecode.api import RhodeCodeApi

# Initialize the RhodeCode API
def create_rhodecode_instance(url, username, password):
    rc = RhodeCodeApi(url, username, password)
    rc.login()
    return rc

# Update a repository with the given information
def update_repository(rc, repo_name, new_name=None, new_description=None):
    # Get the repository details
    repo_details = rc.get_repo(repo_name)
    
    # Update the repository if new name or description is provided
    if new_name:
        repo_details['name'] = new_name
    if new_description:
        repo_details['description'] = new_description
    
    # Update the repository
    rc.update_repo(repo_name, repo_details)

# Define the main function to handle the update operation
def main():
    # Define the RhodeCode instance
    url = "http://localhost:8800"  # Your RhodeCode instance URL
    username = "admin"  # Your RhodeCode username
    password = "password"  # Your RhodeCode password

    # Create an instance of RhodeCode API
    rc = create_rhodecode_instance(url, username, password)

    # Define the repository details
    repo_name = "old-repo-name"

    # Optional: You can provide new name and description for the repository
    new_name = "new-repo-name"
    new_description = "This is a new description"

    # Update the repository
    update_repository(rc, repo_name, new_name, new_description)

if __name__ == "__main__":
    main()
