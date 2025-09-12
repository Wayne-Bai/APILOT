import urllib.request

# Create a URL object
url = urllib.request.urlopen('http://example.com')

# Read the response from the server
response = url.read()

# Print the response
print(response)
