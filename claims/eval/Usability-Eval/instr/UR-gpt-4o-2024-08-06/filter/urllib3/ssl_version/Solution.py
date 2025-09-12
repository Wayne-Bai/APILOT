import urllib3

# Initialize a PoolManager instance to make requests
http = urllib3.PoolManager()

# Define the URL to check the supported SSL versions
url = "https://example.com"

try:
    # Send a GET request to the URL
    response = http.request('GET', url, timeout=5.0)
    
    # Print the status code of the response
    print("Response Status:", response.status)
    
    # Check for TLS protocol versions in the response headers
    print("Supported SSL/TLS version details:")
    
    # This assumes that the server may provide such details in the headers.
    ssl_info = response.headers.get('x-ssl-protocol')
    if ssl_info:
        print(ssl_info)
    else:
        print("SSL/TLS version details not available in headers.")

except urllib3.exceptions.SSLError as e:
    print(f"SSL error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
