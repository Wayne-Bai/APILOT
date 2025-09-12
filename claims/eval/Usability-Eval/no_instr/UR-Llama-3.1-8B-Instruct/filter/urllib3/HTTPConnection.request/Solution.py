# Import the required modules
import urllib3

# Create a PoolManager object
http = urllib3.PoolManager()

# Define the HTTP request method and the request URI
method = 'GET'
url = 'http://www.example.com'  # Example URL, replace with your desired URL

try:
    # Send the request to the server
    response = http.request(method, url)

    # Check if the request was successful
    if response.status == 200:
        print(f'Request successful. Status code: {response.status}')
        print(f'Response text: {response.data.decode()}')
    else:
        print(f'Request failed. Status code: {response.status}')
        print(f'Error message: {response.data.decode()}')
except Exception as e:
    print(f'An error occurred: {e}')
