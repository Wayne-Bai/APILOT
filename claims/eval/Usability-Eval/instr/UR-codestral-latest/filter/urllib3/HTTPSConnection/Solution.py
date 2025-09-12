import urllib3
import ssl
from urllib3.connection import HTTPConnection
from urllib3.util.ssl_ import create_urllib3_context

class SSLHTTPConnection(HTTPConnection):
    def __init__(self, *args, **kwargs):
        ssl_context = create_urllib3_context()
        super(SSLHTTPConnection, self).__init__(*args, port=443, ssl_context=ssl_context, **kwargs)
