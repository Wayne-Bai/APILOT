import urllib3
from urllib.parse import urlparse

def get_proxy_details(url):
    """
    Parse the proxy URL to extract the server name and port.
    
    Args:
    url (str): The proxy URL provided in the format http://<proxy_server>:<port>
    
    Returns:
    tuple: Return a tuple containing proxy server name and port
    """
    parsed_url = urlparse(url)
    proxy_server = parsed_url.hostname
    port = parsed_url.port
    return proxy_server, port

# Example usage
proxy_url = "http://your-proxy-server.com:8080"
server_name, server_port = get_proxy_details(proxy_url)
print("Proxy Server:", server_name)
print("Port:", server_port)
