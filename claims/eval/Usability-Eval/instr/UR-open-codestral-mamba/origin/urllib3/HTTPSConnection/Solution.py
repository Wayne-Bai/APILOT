import urllib3
import ssl

class SSLConnection(urllib3.connection.HTTPConnection):
    def __init__(self, host, port=443, ssl_context=None, *args, **kwargs):
        super().__init__(host, port, *args, **kwargs)
        self.ssl_context = ssl_context

    def connect(self):
        conn = self.ssl_context.wrap_socket(super().connect(), server_hostname=self.host)
        self.sock = conn

# create a SSL context
ssl_context = ssl.create_default_context()

# it turns out that Python's standard SSL context doesn't verify SSL certificates by default
# so we tell it to verify against a some global root CA certificates.
ssl_context.load_default_certs()

# now we pass this SSL context to our secure HTTPSConnection subclass
conn = SSLConnection('python.org', ssl_context=ssl_context)
conn.connect()

# send a HTTP request
conn.request('GET', '/')
resp = conn.getresponse()

# print the result
http_data = resp.read()
print(http_data)
