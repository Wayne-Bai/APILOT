import urllib3

def get_hostname(url):
    # Initialize the HTTP connection pool manager
    http = urllib3.PoolManager()
    
    # Make a request to the URL
    response = http.request('GET', url)
    
    # You can obtain the hostname from the parsed URL in urllib3
    parsed_url = urllib3.util.parse_url(url)
    
    # Return the hostname
    return parsed_url.hostname

# Example usage
url = 'https://example.com/'
hostname = get_hostname(url)
print("Hostname:", hostname)
