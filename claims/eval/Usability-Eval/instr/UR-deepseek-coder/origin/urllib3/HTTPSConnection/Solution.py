import urllib3
import ssl

class SecureHTTPConnection(urllib3.connection.HTTPConnection):
    default_port = 443

    def __init__(self, host, port=None, strict=False, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 source_address=None, blocksize=8192, *, context=None, **kwargs):
        super().__init__(host, port, strict, timeout, source_address, blocksize, **kwargs)
        self.context = context or ssl.create_default_context()

    def connect(self):
        self.sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
        if self._tunnel_host:
            self._tunnel()
        self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)
