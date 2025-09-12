import urllib3

def read_url_data(url, amt=None):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    try:
        data = response.read(amt)
        return data
    finally:
        response.release_conn()

# Example usage:
url = "http://example.com"
data = read_url_data(url, 1024)  # Read up to 1024 bytes
print(data)
