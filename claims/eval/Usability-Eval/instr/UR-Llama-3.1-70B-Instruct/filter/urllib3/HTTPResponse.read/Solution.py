import urllib3

def read_response_body(url, amt=None):
    try:
        # Create a pool manager
        http = urllib3.PoolManager()
        
        # Send a GET request
        response = http.request('GET', url)
        
        # Check if the request was successful
        if response.status == 200:
            # Read the response body, or up to the next amt bytes
            if amt is not None:
                body = response.data[:amt]
            else:
                body = response.data
            
            return body
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
url = 'http://httpbin.org/ip'
response_body = read_response_body(url, amt=100)

if response_body is not None:
    print(response_body)
else:
    print("Failed to retrieve the response body.")
