import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create a URL object with the required identifier
url = "https://example.com"

# Create an HTTP header with the specified identifier
headers = {"X-Header": "headerValue"}

# Configure the SSL context with the SSLkey
ssl_context = create_urllib3_context(verify_ssl=False)  # or change 'verify_ssl=False' to 'True' based on your need

# Set up the HTTP client
http = urllib3.PoolManager(ssl_context=ssl_context)

# Make the request
response = http.request('GET', url, headers=headers)

# Check the response
if response.status == 200:
    print("Request successful")
else:
    print(f"Request failed with status code: {response.status}" + " and response body: " + response.data.decode("utf-8"))
