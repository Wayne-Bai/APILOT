from urllib3 import connection

class SSLHTTPConnection(connection.HTTPConnection):
    def __init__(self, host, port=None, strict=None, timeout=None, proxy_headers=None, context=None):
        super().__init__(host, port, strict, timeout, proxy_headers)
        self.context = context
