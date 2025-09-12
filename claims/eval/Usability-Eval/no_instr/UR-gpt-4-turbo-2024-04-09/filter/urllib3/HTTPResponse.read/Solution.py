import urllib3

def fetch_url_data(url, amt=None):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    
    try:
        data = response.read(amt) if amt is not None else response.read()
        return data
    finally:
        response.release_conn()

# Example usage
url = "http://example.com"
amount_to_read = 500  # Set None to read all
data = fetch_url_data(url, amount_to_read)
print(data)
