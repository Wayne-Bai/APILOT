import urllib3

# Example usage of urllib3
http = urllib3.PoolManager()

# Define your hostname or use None for server-side socket
hostname = 'example.com'

# Define the URL or path
url = '/path/to/resource'

# Define the method (GET, POST, etc.)
method = 'GET'

# Define additional parameters if needed
params = {
    'param1': 'value1',
    'param2': 'value2'
}

headers = {
    'Authorization': 'Bearer your_token',
    'Content-Type': 'application/json'
}

# Send the request
if hostname:
    endpoint = f"https://{hostname}{url}"
else:
    endpoint = "http://localhost:8000/path/to/resource"

try:
    response = http.request(method, endpoint, headers=headers, params=params)

    if response.status == 200:
        print('Success:', response.data.decode('utf-8'))
    else:
        print(f'Error: HTTP Status Code {response.status}')

except urllib3.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.reason}")
