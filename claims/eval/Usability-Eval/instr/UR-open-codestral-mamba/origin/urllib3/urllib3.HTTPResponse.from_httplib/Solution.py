import urllib3
from http.client import HTTPConnection

# Create a urllib3 HTTPConnection object
http = urllib3.PoolManager()

# Create a urllib3 request object
r = http.request('GET', 'http://example.com')  # Replace with your desired URL

# Convert the http.client.HTTPResponse to urllib3.response.HTTPResponse
urllib3_response = urllib3.response.HTTPResponse(
    body=r.read(),
    headers=r.headers,
    status=r.status,
    version=r.version,
    reason=r.reason,
    preload_content=False,
    decode_content=True
)

# Print the urllib3 response object
print(urllib3_response)
