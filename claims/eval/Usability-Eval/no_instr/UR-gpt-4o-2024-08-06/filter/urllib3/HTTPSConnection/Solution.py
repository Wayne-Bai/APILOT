import urllib3
import ssl

class SecureHTTPConnection(urllib3.connection.HTTPConnection):
    default_port = 443

    def __init__(self, host, port=None, context=None, **kwargs):
        if context is None:
            context = ssl.create_default_context()
        self.context = context
        super(SecureHTTPConnection, self).__init__(host, self.default_port if port is None else port, **kwargs)

    def connect(self):
        # Connect to the server and initiate SSL
        self.sock = self._new_conn()
        self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)
        if self._tunnel_host:
            self._tunnel()
