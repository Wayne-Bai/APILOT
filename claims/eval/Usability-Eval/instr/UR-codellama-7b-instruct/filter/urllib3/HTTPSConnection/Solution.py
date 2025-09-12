
class SecureHTTPConnection(urllib3.HTTPSConnection):
    def __init__(self, host, port=443, context=None):
        if context is None:
            context = ssl.create_default_context()
        super().__init__(host, port)
        self._context = context

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((self.host, self.port))
        if self._context:
            ssl_sock = context.wrap_socket(sock, server_hostname=self.host)
        else:
            ssl_sock = ssl.wrap_socket(sock, self.server_hostname)
        self.sock = ssl_sock
        return sock
