import urllib3
import ssl

class HTTPSConnection(urllib3.connection.HTTPConnection):
    default_port = 443

    def __init__(self, host, port=default_port, context=None, **kwargs):
        super().__init__(host, port, **kwargs)
        self.context = context or ssl.create_default_context()

    def connect(self):
        self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)
