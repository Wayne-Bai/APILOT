import urllib3
import ssl

class SecureHTTPConnection(urllib3.connection.HTTPSConnection):
    def __init__(self, host, port=443, context=None, *args, **kwargs):
        if context is None:
            context = ssl.create_default_context()
        super().__init__(host, port, strict=True, *args, **kwargs)
        self.context = context

    def connect(self):
        """Establish a secure connection using the SSL context."""
        self.sock = self._create_connection((self.host, self.port), self.timeout)
        self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)
