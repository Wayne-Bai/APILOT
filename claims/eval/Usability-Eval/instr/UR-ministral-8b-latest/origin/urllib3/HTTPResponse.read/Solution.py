import urllib3

def fetch_partial_response(url, num_bytes):
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    if response.status != 200:
        raise Exception(f"HTTP request failed with status {response.status}")

    return response.data[:num_bytes].decode('utf-8')

# Usage example
url = "https://example.com"
num_bytes = 100
partial_response = fetch_partial_response(url, num_bytes)
print(partial_response)
