import urllib3

def fetch_http_headers(url):
    # Create a PoolManager instance to make requests
    http = urllib3.PoolManager()

    # Make a GET request to the specified URL
    response = http.request('GET', url)

    # Get the headers from the response
    headers = response.headers

    # Create an unmodifiable view by converting the dictionary to a frozenset
    unmodifiable_headers = frozenset(headers.items())

    return unmodifiable_headers

# Example usage
url = "http://www.example.com"
headers_view = fetch_http_headers(url)
for header, value in headers_view:
    print(f"{header}: {value}")
