import urllib3

def fetch_data(url, amt=1024):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    
    try:
        data = response.read(amt)
    finally:
        response.release_conn()

    return data

# Example usage:
url = 'http://www.example.com'
data = fetch_data(url, amt=512)
print(data.decode('utf-8'))
