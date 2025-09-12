import requests

# Make a simple GET request to a url
response = requests.get('http://example.com')

# Get a view of the response headers
headers = response.headers

# Print the headers
for key, value in headers.items():
    print(key, ':', value)
