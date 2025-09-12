import urllib3

def fetch_http_headers(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Fetch headers and display them in an unmodifiable view
    headers = response.headers
    for key, value in headers.items():
        print(f"{key}: {value}")

# Example usage
fetch_http_headers('http://example.com')
