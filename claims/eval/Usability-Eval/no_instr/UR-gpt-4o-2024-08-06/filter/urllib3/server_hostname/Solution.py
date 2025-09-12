import urllib3

def get_server_hostname(url):
    # Create a PoolManager instance to make requests
    http = urllib3.PoolManager()

    try:
        # Make a request to the server
        response = http.request('HEAD', url)
        
        # Extract the hostname from the request object
        hostname = response.retries.host or None
    except Exception as e:
        print(f"An error occurred: {e}")
        hostname = None
        
    return hostname

# Example usage
url = "http://www.example.com"
hostname = get_server_hostname(url)
print(f"Hostname of the server: {hostname}")
