from rhodecode import APIConnection

def get_repository_members(api_key,server):
    try:
        repo = APIConnection(api_key, server)
        response = repo.repos_get(domain='', bare=True, repo_name_or_id=None, include='members')

        repository = response.get('repository', {})

        if not repository:
            print("Error: Repository not found.")
            return

        members = repository.get('members', [])

        if not members:
            print("Error: No members found in the repository.")
            return

        members_info = []
        for member in members:
            try:
                member_info = repo.users_get(domain='', username=member)
                members_info.append(member_info['repository_memberships'])
            except Exception as e:
                print(f"Error fetching member details for {member}: {str(e)}")

        print("Repository Members Info:")
        for info in members_info:
            print(info)

    except Exception as e:
        print(f"Error: {str(e)}")

# example usage:
# API connection details
api_key = 'your_api_key'
server = 'https://your_rhodecode_server'

# Call the function
get_repository_members(api_key, server)
