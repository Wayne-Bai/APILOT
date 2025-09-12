# Import the urllib3 library
import urllib3

# Initialize the PoolManager
http = urllib3.PoolManager()

# Send a GET request to a specified URL
def get_http_headers(url):
    try:
        response = http.request('GET', url)

        # Get the HTTP headers and corresponding values
        http_headers = response.get_headers()

        # Print the HTTP headers
        for header, value in http_headers.items():
            print(f"{header}: {value}")

    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

# Test the function
get_http_headers('http://www.example.com')

# Alternative way to get headers only using response.info()
def get_http_headers_info(url):
    try:
        response = http.request('GET', url)
        http_headers_info = response.info()
        
        # Print the HTTP headers
        for header, value in http_headers_info.items():
            print(f"{header}: {value}")

    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

# Test the alternative function
get_http_headers_info('http://www.example.com')
