# Import httpx library
import httpx

# Send a GET request to a URL
def get_headers(url):
    try:
        # Make GET request
        response = httpx.get(url)

        # Check if the GET request was successful
        if response.status_code == 200:
            # Return a dictionary of HTTP headers
            return response.headers
        else:
            # If GET request was not successful, print the status code and return None
            print("HTTP status code:", response.status_code)
            return None
    except Exception as e:
        # If an exception occurs, print the error message and return None
        print("Error:", str(e))
        return None

# Usage example
url = "http://example.com"
headers = get_headers(url)
if headers is not None:
    for key, value in headers.items():
        print(f'{key}: {value}')
