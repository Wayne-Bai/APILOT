import rhodecode

def get_repository_with_members(api_client, repo_identifier):
    try:
        # Fetch repository details by name or repository_id
        repo_details = api_client.get_repo(repo_id=repo_identifier)
        
        # Check if the repository was found
        if 'repository' not in repo_details:
            print("Repository not found")
            return None
        
        # Fetching the members (user groups or users associated with the repository)
        repo_id = repo_details['repository']['repo_id']
        members = api_client.get_repo_members(repo_id=repo_id)
        
        # Print details about members
        if members.get('members'):
            for member in members['members']:
                print(f"Member Type: {member.get('type')}, Name: {member.get('name')}")
        else:
            print("No members found for this repository")
        
        return members
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example of initializing RhodeCode API client
# You will need your specific api_key and api_url
api_url = "https://your-rhodecode-instance/api/"
api_key = "your_api_key"
client = rhodecode.RhodeCodeAPI(api_url=api_url, api_key=api_key)

# Fetch repository and its members using the name or repository_id
repository_identifier = "your_repository_name_or_id"
get_repository_with_members(client, repository_identifier)
