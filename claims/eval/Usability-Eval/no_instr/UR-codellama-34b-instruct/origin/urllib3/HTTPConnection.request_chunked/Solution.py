import urllib3

# Set up the HTTP connection
http = urllib3.PoolManager()

# Define the URL and data to be sent
url = 'https://example.com'
data = {'key': 'value', 'key2': 'value2'}

# Encode the data as a chunked request
chunked_data = urllib3.encode_chunked(data)

# Set up the HTTP headers for the request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Transfer-Encoding': 'chunked'
}

# Make the request
response = http.request('POST', url, body=chunked_data, headers=headers)

# Print the response data
print(response.data)
