import urllib3
import ssl

# Create an SSL context with hostname checking enabled
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

# Create a pool manager with the custom SSL context
http = urllib3.PoolManager(
    ssl_context=context,
    cert_reqs=ssl.CERT_REQUIRED,
)

def get_url(url, hostname):
    try:
        # Make a request to the URL, passing the hostname for verification
        response = http.request('GET', url, preload_content=False, assert_same_host=hostname)
        
        if response.status == 200:
            print(" TLS handshake successful with hostname verification")
        else:
            print(" TLS handshake failed with hostname verification")
        
        # close the response to free up resources
        response.release_conn()
        
    except urllib3.exceptions.SSLError as e:
        print(" SSL error occurred: ", e)

# Example usage
get_url("https://www.example.com", "www.example.com")
