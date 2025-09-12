
import urllib3
from socket import create_connection

def make_https_request(url):
    """
    Make an HTTPS request to the given URL.
    If SNI is not available, use the `create_connection` function from the `socket` module
    to establish a connection and then wrap it in an SSL/TLS context using the `ssl` module.
    """
    try:
        # Try making the request with SNI
        response = urllib3.urlopen(url, timeout=10)
    except urllib3.exceptions.SSLError:
        # If SNI is not available, use `create_connection` to establish a connection
        # and then wrap it in an SSL/TLS context using the `ssl` module.
        conn = create_connection((url, 443))
        context = ssl.create_default_context()
        wrapped_conn = context.wrap_socket(conn, server_hostname=url)
        response = urllib3.urlopen(wrapped_conn, timeout=10)
    return response
