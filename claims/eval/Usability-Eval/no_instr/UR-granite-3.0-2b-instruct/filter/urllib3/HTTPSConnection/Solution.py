import urllib3

class SSLHTTPConnection(urllib3.HTTPConnection):
    def __init__(self, host, port, *args, **kwargs):
        super().__init__(host, port, *args, **kwargs)
        self.ssl_context = urllib3.util.ssl_.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
