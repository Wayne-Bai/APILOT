
import rhodecode

# Connect to the RhodeCode instance
rc = rhodecode.connect(url='https://your-rhodecode-instance-url.com', api_token='your-api-token')

# Define the repository information
repo_name = 'your_repository_name'
new_description = 'new_repository_description'
new_visibility = 'private'  # 'public' or 'private'

# Get the repository by name
repo = rc.api.repository.get(repo_name)

# Update the repository information
rc.api.repository.update(repo_name, description=new_description, visibility=new_visibility)

print(f'Repository {repo_name} has been updated with new description and visibility.')
