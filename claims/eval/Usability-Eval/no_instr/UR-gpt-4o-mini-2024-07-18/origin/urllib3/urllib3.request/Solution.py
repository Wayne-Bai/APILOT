import urllib3

def make_request(url):
    # Create a new PoolManager instance to avoid shared state
    http = urllib3.PoolManager()

    # Make a GET request
    response = http.request('GET', url)

    # Return the response data
    return response.data

# Example usage
if __name__ == "__main__":
    url = 'http://example.com'
    response_data = make_request(url)
    print(response_data)
