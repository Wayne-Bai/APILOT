# Import the required library
from urllib3 import HTTPResponse
import urllib3

# Create an HTTP client
http = urllib3.PoolManager()

# Send a GET request to a URL (replace 'http://www.example.com' with the desired URL)
response = http.request('GET', 'http://www.example.com')

# Return an unmodifiable view of the HTTP headers and corresponding values
headers = response.headers

# Print the HTTP headers
for key, value in headers.items():
    print(f"{key}: {value}")
