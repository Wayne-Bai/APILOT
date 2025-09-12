Python
import urllib3
import json

# Define your URL and data here
url = "http://example.com"
data = {'key': 'value'}

# Create a pool manager
http = urllib3.PoolManager()

# Encode the data
encoded_data = json.dumps(data).encode('utf-8')

# Create a request
response = http.request(
    'POST',
    url,
    body=encoded_data,
    headers={'Content-Type': 'application/json', 'Content-Length': len(encoded_data)},
)

# Print the response status
print(response.status)

# Decode and load JSON from the response if it's a JSON response
if response.headers.get('content-type') == 'application/json':
    json_data = json.loads(response.data.decode('utf-8'))
    print(json_data)
