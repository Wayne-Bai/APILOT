import urllib3
import ssl

class SecureHTTPConnection(urllib3.connection.HTTPConnection):
    default_port = 443

    def __init__(self, host, port=None, strict=False, timeout=None, ssl_context=None, **kwargs):
        if ssl_context is None:
            ssl_context = ssl.create_default_context()
        super().__init__(host, port or self.default_port, strict, timeout, **kwargs)
        self.ssl_context = ssl_context

    def connect(self):
        self.sock = self.ssl_context.wrap_socket(
            super().connect(),
            server_hostname=self.host
        )
