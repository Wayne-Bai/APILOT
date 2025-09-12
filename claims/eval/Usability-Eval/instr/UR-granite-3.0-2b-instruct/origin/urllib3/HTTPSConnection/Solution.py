import urllib3

class SecureHTTPConnection(urllib3.PoolManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self.context.check_hostname = True
        self.context.verify_mode = ssl.CERT_REQUIRED

    def _make_connection(self, host, port, **kwargs):
        context = self.context
        return context.wrap_socket(super()._make_connection(host, port, **kwargs), server_hostname=host)
