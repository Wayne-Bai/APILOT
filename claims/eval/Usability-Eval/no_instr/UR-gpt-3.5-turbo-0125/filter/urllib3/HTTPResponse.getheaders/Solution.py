
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://www.example.com')

if response.headers:
    headers = response.headers

    # Create a dictionary from the headers
    headers_dict = dict(headers.items())

    # Function to return an unmodifiable view of the headers
    def get_unmodifiable_headers():
        return headers_dict

    # Test the function
    unmodifiable_headers = get_unmodifiable_headers()
    print(unmodifiable_headers)

else:
    print('No headers found in the response.')
