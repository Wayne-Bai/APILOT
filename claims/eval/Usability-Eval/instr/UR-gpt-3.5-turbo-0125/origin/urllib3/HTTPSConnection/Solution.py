
import urllib3
import ssl

class MyHTTPSConnection(urllib3.connection.HTTPSConnection):
    default_port = 443

    def __init__(self, *args, context=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = context

    def connect(self):
        self.sock = socket.create_connection(
            (self.host, self.port), self.timeout, self.source_address
        )
        if self.context is None:
            self.sock = ssl.wrap_socket(self.sock, self.key_file, self.cert_file,
                                        cert_reqs=self.cert_reqs, ca_certs=self.ca_certs,
                                        server_hostname=self.server_hostname)
        else:
            self.sock = self.context.wrap_socket(self.sock, server_hostname=self.server_hostname)

urllib3.connectionpool.HTTPSConnection = MyHTTPSConnection
