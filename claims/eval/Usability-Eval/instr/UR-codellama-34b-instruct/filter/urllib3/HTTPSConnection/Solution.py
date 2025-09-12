
import urllib3
from urllib3 import PoolManager

class HTTPSConnection(urllib3.HTTPConnection):
    def __init__(self, host, port=443, context=None, **kwargs):
        self.context = context
        if not isinstance(context, ssl.SSLContext):
            raise ValueError("Context must be an instance of ssl.SSLContext")
        super().__init__(host, port, **kwargs)

    def connect(self):
        sock = socket.socket()
        sock.connect((self.host, self.port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.context is not None:
            sock.starttls(self.context)
        return sock
