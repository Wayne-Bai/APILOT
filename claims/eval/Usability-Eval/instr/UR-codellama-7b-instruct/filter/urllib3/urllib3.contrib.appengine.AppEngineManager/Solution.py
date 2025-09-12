
import urllib3

class ConnectionManager:
    def __init__(self):
        self.pool = urllib3.PoolManager(timeout=5)

    def request(self, method, url, **kwargs):
        return self.pool.request(method, url, **kwargs)
