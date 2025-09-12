import ssl
import urllib3

class HTTPSConnectionWithSSLContext(urllib3.connection.HTTPSConnection):
    default_port = 443

    def __init__(self, host, port=None, context=None, **kwargs):
        self.ssl_context = context or ssl.create_default_context()
        super().__init__(host, port=port or self.default_port, **kwargs)

    def connect(self):
        self.sock = self._new_conn()
        self.sock = self._ssl_wrap_socket(self.sock, self.host, self.port)

    def _ssl_wrap_socket(self, sock, server_hostname, port):
        return self.ssl_context.wrap_socket(sock, server_hostname=server_hostname)

# Example usage:
# context = ssl.create_default_context()
# conn = HTTPSConnectionWithSSLContext('www.example.com', context=context)
