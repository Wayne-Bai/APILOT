
import http.client
import json

# Set up the HTTP client
http_client = http.client.HTTPConnection('www.example.com')

# Set up the JSON payload
payload = {'key': 'value'}
json_payload = json.dumps(payload)

# Set the headers
headers = {
    'Content-Type': 'application/json',
    'Content-Length': str(len(json_payload))
}

# Make the POST request
http_client.request('POST', '/path/to/resource', json_payload, headers)
response = http_client.getresponse()

# Check the status code
if response.status == 200:
    print("Request sent successfully")
else:
    print(f"Error sending request: {response.reason}")
