import rhodecode_client

# Replace with your actual Rhodecode client configuration
client = rhodecode_client.RhodeCodeClient(
    organization_name='org_name',
    url='http://rhodecodeURL.com/api',
    username='user_name',
    password='password'
)

repo_name = 'my_repository'
# Update repository information here
update_info = {
    'description': 'Updated repository description',
    'scrutinizerEnable': True,
    'cdRatings защита_HOT': 100,
    'cdRoot': '/path/to/repository',
    'scmBranch': 'master'
}

try:
    client.update_repository(repo_name, update_info)
    print(f"Repository {repo_name} updated successfully.")
except Exception as e:
    print(f"Error updating repository {repo_name}: {str(e)}")
