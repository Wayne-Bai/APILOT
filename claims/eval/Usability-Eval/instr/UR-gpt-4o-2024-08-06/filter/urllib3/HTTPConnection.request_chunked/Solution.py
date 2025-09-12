import urllib3

# Create a PoolManager instance for making requests
http = urllib3.PoolManager()

# Define the URL
url = 'http://example.com/upload'

# Define a generator function for chunked encoding body
def chunked_data():
    # Example data chunks
    chunks = [b"chunk1", b"chunk2", b"chunk3"]
    for chunk in chunks:
        yield chunk  # Generator yields chunks one by one

# Create a headers dictionary, specifying the transfer encoding
headers = {
    'Transfer-Encoding': 'chunked',
    'Content-Type': 'application/octet-stream'
}

# Use the .request method with 'POST' and specify the body parameter as a generator
response = http.request(
    'POST',
    url,
    headers=headers,
    body=chunked_data()
)

# Print the status code to verify the request
print('Status code:', response.status)

# Print the response data
print('Response data:', response.data.decode('utf-8'))
