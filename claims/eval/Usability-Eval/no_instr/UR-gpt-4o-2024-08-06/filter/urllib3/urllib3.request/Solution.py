import urllib3

def fetch_data(url):
    # Create a new PoolManager instance to manage HTTP connections
    http = urllib3.PoolManager()

    # Make a GET request to the given URL
    response = http.request('GET', url)

    # Check if the request was successful
    if response.status == 200:
        # Return the data
        return response.data
    else:
        # Return an error message
        return f"Failed to fetch data: {response.status}"

# Example usage
url = "http://example.com"
data = fetch_data(url)
print(data.decode('utf-8'))
