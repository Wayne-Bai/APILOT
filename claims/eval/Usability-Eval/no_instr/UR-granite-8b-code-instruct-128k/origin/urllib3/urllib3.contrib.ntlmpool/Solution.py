
import urllib3

# Define the function to authenticate with NTLM
def authenticate_with_ntlm(url, username, password):
    # Create an instance of the HTTP pool manager
    http = urllib3.PoolManager()

    # Set the authentication header
    headers = {
        'Authorization': f'NTLM {username}:{password}'
    }

    # Make a request to the URL
    response = http.request('GET', url, headers=headers)

    # Print the response body
    print(response.data.decode('utf-8'))

# Call the function to authenticate with NTLM
authenticate_with_ntlm('http://example.com', 'username', 'password')
