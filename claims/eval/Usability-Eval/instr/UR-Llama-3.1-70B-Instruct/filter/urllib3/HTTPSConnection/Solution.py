import urllib3
import ssl

class HTTPSConnection(urllib3.connectionpool.HTTPSConnection):
    def __init__(self, host, port=None, key_file=None, cert_file=None, 
                 ca_file=None, timeout=None, context=None):
        
        if context is None:
            context = ssl.create_default_context()
        
        self.ssl_context = context
        super().__init__(host, port, key_file, cert_file, ca_file, timeout)

    def connect(self):
        context = self.ssl_context
        host = self.host
        port = self.port

        if not port:
            port = 443

        # wrap socket to use TLS
        try:
            self.sock = context.wrap_socket(self.sock, server_hostname=host)
        except AttributeError:
            self.sock = context.wrap_socket(self.sock)

        # We have to explicitly set the timeout after wrap_socket.
        self.sock.settimeout(self.timeout)

def usage_example():
    https = HTTPSConnection(host='www.example.com')
    try:
        https.connect()
        print(f"Connected to {https.host}:{https.port} over SSL")
    except Exception as e:
        print(f"Failed to connect to {https.host}:{https.port} over SSL: {e}")
    finally:
        https.close()

if __name__ == "__main__":
    usage_example()
