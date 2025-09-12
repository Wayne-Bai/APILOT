import urllib3
from urllib3.poolmanager import PoolManager

class SecureHTTPConnection(urllib3.poolmanager.HTTPConnection):
    def __init__(self, *args, **kwargs):
        self.context = kwargs.pop('context', None)
        super().__init__(*args, **kwargs)

    def connect(self):
        if self.context:
            self.conn = self.context.wrap_socket(
                self.sock,
                server_hostname=self.host
            )
        else:
            super().connect()

# Usage
http = SecureHTTPConnection(host='example.com', context=ssl.create_default_context())
http.request('GET', '/')
