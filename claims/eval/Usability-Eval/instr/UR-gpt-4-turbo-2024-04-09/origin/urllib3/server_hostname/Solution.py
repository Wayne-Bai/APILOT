import urllib3

def get_hostname(url):
    try:
        # Create a PoolManager instance
        http = urllib3.PoolManager()

        # Parse the URL to get the hostname
        parsed_url = urllib3.util.parse_url(url)
        hostname = parsed_url.host

        # Return the hostname, or None if it wasn't specified
        return hostname

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
url = "http://example.com"
hostname = get_hostname(url)
print("Hostname:", hostname)
