import urllib3

# Create a PoolManager instance to make requests.
http = urllib3.PoolManager()

# Define the URL and the data to be sent in chunks.
url = 'http://example.com/api'
data = [
    ('chunk1', 'This is the first chunk of data.'),
    ('chunk2', 'This is the second chunk of data.'),
    ('chunk3', 'This is the third chunk of data.')
]

# Create a request with chunked encoding.
response = http.request(
    'POST',
    url,
    body=data,
    headers={'Transfer-Encoding': 'chunked'}
)

# Print the response status and data.
print(f'Response Status: {response.status}')
print(f'Response Data: {response.data.decode("utf-8")}')
