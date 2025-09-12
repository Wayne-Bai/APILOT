
import http.client

url = 'https://example.com'

# Send a GET request
response = http.client.HTTPConnection(url).getresponse()

# Print the response body
print(response.read())
