import urllib3

# Create a custom TLS backend using pyOpenSSL
class OpenSSLTLS(urllib3.TLS):
    def __init__(self):
        import OpenSSL
        self._ssl = OpenSSL.SSL.Context(self.method)

    def socket(self, sock, host, port, ssl_params=None):
        ctx = self._ssl.wrap_socket(sock, server_side=False, ssl_version=self.ssl_version, **ssl_params)
        return ctx

# Set the custom TLS backend
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_TLS_VERSION = urllib3.util.ssl_.TLSv1_2
urllib3.util.ssl_.DEFAULT_TLS_BACKEND = OpenSSLTLS()
