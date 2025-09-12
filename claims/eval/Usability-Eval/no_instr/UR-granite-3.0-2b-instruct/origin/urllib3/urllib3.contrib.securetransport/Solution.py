import urllib3

# Create a custom SSLContext
ssl_context = urllib3.SSLContext(ssl.SSLProtocolVersion.LATEST)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

# Create a custom HTTPConnectionPool
class CustomHTTPConnection(urllib3.PoolManager.HTTPConnection):
    def establish_connection(self, host, port, timeout, **kwargs):
        httplib = urllib3.PoolManager.HTTPConnection.establish_connection(self, host, port, timeout, **kwargs)
        httplib.ssl_socket = ssl_context.wrap_socket(httplib.sock, server_hostname=host)
        return httplib

# Create a custom HTTPConnectionPool with the custom HTTPConnection class
http = urllib3.PoolManager(http_connection_class=CustomHTTPConnection)

# Now you can use the http object to make HTTPS requests
response = http.request('GET', 'https://example.com')
