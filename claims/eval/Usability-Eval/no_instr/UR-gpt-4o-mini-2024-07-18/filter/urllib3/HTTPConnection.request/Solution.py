import urllib3

def send_request(method, url):
    # Create a PoolManager instance to handle the connections
    http = urllib3.PoolManager()

    # Send the request
    response = http.request(method, url)

    # Return the response data
    return response.data

# Example usage
if __name__ == "__main__":
    method = 'GET'  # Specify the HTTP method (GET, POST, etc.)
    url = 'http://example.com'  # Replace with the desired absolute URL
    
    response_data = send_request(method, url)
    print(response_data)
