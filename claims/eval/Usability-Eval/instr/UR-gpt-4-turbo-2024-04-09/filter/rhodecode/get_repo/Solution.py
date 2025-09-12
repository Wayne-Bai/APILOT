import rhodecode

def get_repository_members(repo_name_or_id):
    # Initialize API client - replace 'api_key' and 'api_url' with actual values
    api_client = rhodecode.RhodeCodeAPI(api_key='YOUR_API_KEY', api_url='https://your-rhodecode-instance/api/')
    
    try:
        # Fetch repository information by name or ID
        repo_info = api_client.get_repo(repo_name_or_id)
        
        # Repository permissions indicating associated users/groups
        repository_permissions = repo_info['permissions']
        
        # Output the list of associated users and groups along with their permission levels
        for permission in repository_permissions:
            perm_type, name, access_level = permission['type'], permission['name'], permission['permission']
            print(f"{perm_type.capitalize()} '{name}' has {access_level} access.")
    
    except Exception as e:
        print(f"Error accessing repository: {str(e)}")
        
# Example usage:
get_repository_members('your-repository-name-or-id')
