
import urllib3

# Create a HTTP connection pool
http = urllib3.PoolManager()

# Make a GET request to a URL
response = http.request('GET', 'https://www.example.com/')

# Get the status code and headers from the response
status_code = response.status_code
headers = dict(response.getheaders())

# Print the status code and headers
print("Status Code:", status_code)
print("Headers:")
for key, value in headers.items():
    print("  {}: {}".format(key, value))

# Get the response body as a string
body = response.data.decode('utf-8')

# Print the response body
print("Body:", body)
