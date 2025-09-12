import requests

# Create a request object and pass the url and headers
url = "http://example.com"
response = requests.get(url)

# Get the value of a header
header_value = response.headers.get('Content-Type')

print(header_value)
