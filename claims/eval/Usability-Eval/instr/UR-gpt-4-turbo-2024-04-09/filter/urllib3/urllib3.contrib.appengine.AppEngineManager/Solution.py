import urllib3

def create_connection_pool():
    # Create a connection pool manager
    http = urllib3.PoolManager()

    # Example URL
    url = 'https://www.example.com/'

    try:
        # Sending a request
        response = http.request('GET', url)
        
        # Print response data
        print(f'Status code: {response.status}')
        print(f'Response body: {response.data.decode("utf-8")}')
    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release the resources
        http.clear()

if __name__ == '__main__':
    create_connection_pool()
