import urllib3

def fetch_response_data(url, amt):
    # Create a PoolManager instance to make requests
    http = urllib3.PoolManager()

    # Make a GET request to the specified URL
    response = http.request('GET', url, preload_content=False)

    try:
        # Define a generator to read up to amt bytes from the response
        data = response.stream(amt)
        for chunk in data:
            print(chunk.decode('utf-8'))
    finally:
        # Ensure that the response is properly closed
        response.release_conn()

# Example usage:
fetch_response_data('http://example.com', 1024)
