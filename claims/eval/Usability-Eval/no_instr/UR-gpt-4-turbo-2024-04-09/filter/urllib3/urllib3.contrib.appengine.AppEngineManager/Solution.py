import urllib3

def create_connection_manager():
    # Create a urllib3.PoolManager instance to handle connections.
    http = urllib3.PoolManager()

    return http

def fetch_url(http, url):
    # Use the connection manager to make HTTP requests.
    response = http.request('GET', url)
    return response

# Main execution setup
if __name__ == "__main__":
    # URL to fetch; example URL
    test_url = 'https://example.com'

    # Create a connection manager
    http_manager = create_connection_manager()

    # Fetch the content of the URL
    response = fetch_url(http_manager, test_url)

    # Output the data received
    print('Status Code:', response.status)
    print('Headers:', response.headers)
    print('Body:', response.data.decode('utf-8'))
