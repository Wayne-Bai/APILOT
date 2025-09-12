import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the data to send
data = b'This is a sample request body that we will send in chunks.'

# Define a generator to yield the data in chunks
def chunked_data(data, chunk_size=10):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Send a POST request with chunked encoding
url = 'http://httpbin.org/post'  # Example URL, replace with your target URL
response = http.request(
    'POST',
    url,
    body=chunked_data(data),
    headers={'Transfer-Encoding': 'chunked'}
)

# Print the response
print(response.data.decode('utf-8'))
