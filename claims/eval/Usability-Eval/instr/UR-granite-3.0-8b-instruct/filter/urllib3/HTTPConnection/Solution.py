import urllib3

# Create an HTTP connection to www.google.com
http = urllib3.PoolManager()

# Send a GET request to www.google.com
response = http.request('GET', 'http://www.google.com')

# Print the status code of the response
print(response.status)

# Print the content of the response
print(response.data.decode('utf-8'))
