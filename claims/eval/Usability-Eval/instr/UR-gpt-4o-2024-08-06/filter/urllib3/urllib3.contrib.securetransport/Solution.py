import urllib3

# Create a PoolManager instance to handle the HTTP requests
http = urllib3.PoolManager()

# Example HTTPS request to demonstrate TLS functionality
url = 'https://www.example.com'

try:
    # Send a GET request to the specified URL
    response = http.request('GET', url)
    
    # Print the status code and response data
    print(f'Status Code: {response.status}')
    print(f'Response Data: {response.data.decode("utf-8")}')
    
except urllib3.exceptions.HTTPError as e:
    # Handle any HTTP errors
    print(f'HTTP error occurred: {e}')
