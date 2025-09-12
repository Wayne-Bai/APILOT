import urllib3

# Replace this with your own URL and method
url = "http://www.example.com"
method = "GET"

# Create an HTTP request object
req = urllib3.Request(url, method)

# Send the request to the server
resp = urllib3.urlopen(req)

# Print the response status code and content
print(resp.status_code)
print(resp.content)
