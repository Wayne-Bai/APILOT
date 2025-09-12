# Importing rhodecode APIs
from rhodecode_api.repositories import update_repository

# Content that you want to update
new_description = 'New Description'
new_file_content = 'New file content'

# Updating the repository
def update_repository_info(repo_id, new_description, new_file_content):
    # Get repository information
    repo_info = repository_get(repo_id)

    # Update repository description
    repo_info.description = new_description
    repo_info.commit()

    # Update the content of a specific file in the repository
    repo_file = repo_info.get_file('file_name.py')  # Replace 'file_name.py' with the name of the file you want to update
    repo_file.update_content(new_file_content)
    repo_file.commit()
