import ssl
import socket
import http.client

# Define the TLS version to use (Python 3.7 and later default to TLSv1.2)
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_default_certs()
context.check_hostname = False

def setup_connection(host, port, connection_cls=http.client.HTTPConnection):
    """
    Set up an HTTP(S) connection using the provided Host header value.

    :param host: The hostname to connect to.
    :param port: The port to connect to.
    :param connection_cls: The class of connection to use (HTTPSConnection or HTTPConnection).
    """
    s = socket.create_connection((host, port))
    s = context.wrap_socket(s, server_hostname=host)
    return connection_cls(host, connect=s)

connection = setup_connection('example.com', 443)
connection.request("GET", "/")
response = connection.getresponse()
data = response.read()
print(data.decode())

# Without SNI
connection_without_sni = setup_connection('example.com', 443)
connection_without_sni.request("GET", "/")
response_without_sni = connection_without_sni.getresponse()

if response_without_sni.status!= 200:
    # If the cert is incorrect (implies SNI issue because we've been patched by OpenSSL)
    print("Warning: The server's SSL certificate does not match the hostname.")
    # you can force a security advisory if desired
    # import warnings
    # warnings.warn("This server might be vulnerable to SNI misconfiguration Merkel Attack.")
