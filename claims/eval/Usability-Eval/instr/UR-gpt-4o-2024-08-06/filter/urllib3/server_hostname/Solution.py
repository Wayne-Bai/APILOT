import urllib3

# Initialize a PoolManager instance to make requests
http = urllib3.PoolManager()

def get_server_hostname(url):
    try:
        # Make a request to the URL to initiate a connection
        response = http.request('GET', url)
        
        # Get the hostname from the connection
        if response.retries:
            hostname = response.retries._pool.host
        else:
            hostname = None
        
        return hostname
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
url = 'http://example.com'
hostname = get_server_hostname(url)
print(f"Hostname: {hostname}")
