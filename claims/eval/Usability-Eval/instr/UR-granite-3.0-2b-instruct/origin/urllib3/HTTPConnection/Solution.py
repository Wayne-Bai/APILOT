import urllib3

http = urllib3.PoolManager()

# Create a connection to the server
with http.request('GET', 'https://www.example.com') as response:
    # Get the status code and content
    status_code = response.status
    content = response.data

    # Print the status code and content
    print(f'Status code: {status_code}')
    print(f'Content: {content}')
