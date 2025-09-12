import urllib3
import json

# Create aputation
http = urllib3.PoolManager()

# The URI to send the request to
url = 'http://example.com/api'

# The chunked data to be sent
chunked_data = [
    b'{"key1": "value1", "key2": "value2"}\r\n',
    b'{"key3": "value3"}\r\n',
    b'{"key4": "value4"}\r\n'
]

# Build the headers and prepare the data
headers = {
    'Content-Type': 'application/json',
    'Transfer-Encoding': 'chunked'
}

# Sending requests with chunked encoding
def send_chunked_request(chunked_data, headers):
    http.request('POST', url, headers=headers, body=b''.join(chunked_data))

# Invoke the request function
send_chunked_request(chunked_data, headers)
