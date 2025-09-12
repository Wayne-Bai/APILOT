import urllib3

def get_proxied_server_info(url):
    """
    Retrieves the name and port of a proxied server as specified in the proxy_pass directive.

    Args:
        url (str): The URL of the proxied server.

    Returns:
        tuple: A tuple containing the name and port of the proxied server.
    """

    # Create a PoolManager instance to connect to the proxied server
    http = urllib3.ProxyManager(url)

    # Send a request to the proxied server
    try:
        response = http.request('GET', url)
    except urllib3.exceptions.MaxRetryError as e:
        print(f"Failed to connect to the proxied server: {e}")
        return None

    # Check if the response is successful
    if response.status!= 200:
        print(f"Failed to retrieve server information: {response.status}")
        return None

    # Get the URL of the proxied server from the response headers
    proxied_server_url = response.headers.get('X-Proxy-URL')

    # Extract the name and port of the proxied server from the URL
    if proxied_server_url:
        proxied_server_name = proxied_server_url.split(':')[0]
        proxied_server_port = proxied_server_url.split(':')[1]

        return proxied_server_name, proxied_server_port
    else:
        return None

# Example usage
url = "http://example.com:8080"
proxied_server_info = get_proxied_server_info(url)

if proxied_server_info:
    print(f"Proxied server name: {proxied_server_info[0]}")
    print(f"Proxied server port: {proxied_server_info[1]}")
