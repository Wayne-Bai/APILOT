from urllib3 import HTTPConnection, Context

# Example usage
conn = HTTPConnection('www.example.com', port=80, timeout=5, source=('localhost', 854)) # Replace with actual host and source
conn.request('GET', '/', headers={'User-Agent': 'my-app/0.0.1'})
response = conn.getresponse()

if response.status == 200:
    print("Request was successful")
    print(response.data.decode('utf-8'))
else:
    print(f"Request failed with status code: {response.status}")
