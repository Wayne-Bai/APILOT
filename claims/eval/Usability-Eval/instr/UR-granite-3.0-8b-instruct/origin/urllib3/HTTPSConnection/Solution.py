import ssl
import urllib3

class SSLHTTPConnection(urllib3.HTTPConnection):
    def __init__(self, host, port=443, context=None, **kwargs):
        if context is not None and not isinstance(context, ssl.SSLContext):
            raise ValueError("Context must be a ssl.SSLContext instance")
        super().__init__(host, port, **kwargs)
        if context is not None:
            self.sock = ssl.create_default_context(ssl.Purpose.SERVER_AUTH).wrap_socket(self.sock, server_hostname=host)
