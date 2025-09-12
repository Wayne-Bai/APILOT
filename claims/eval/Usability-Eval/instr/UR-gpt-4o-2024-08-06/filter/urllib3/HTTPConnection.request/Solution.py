import urllib3

def send_request(url, method='GET'):
    http = urllib3.PoolManager()
    
    try:
        # Make a request to the server using the provided HTTP method and absolute URL
        response = http.request(method, url)

        # Print status code and response data
        print(f'Status Code: {response.status}')
        print(f'Response Data: {response.data.decode("utf-8")}')
        
    except urllib3.exceptions.HTTPError as e:
        print(f'HTTP error occurred: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Clean up the connection
        http.clear()

# Example usage
# Ensure your URL is an absolute path
url = 'http://www.example.com'
send_request(url)
