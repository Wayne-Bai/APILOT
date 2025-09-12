import urllib3

class ConnectionManager:
    def __init__(self):
        self.pool_manager = urllib3.PoolManager()

    def get(self, url):
        r = self.pool_manager.request('GET', url)
        return r.data

    def post(self, url, fields):
        r = self.pool_manager.request('POST', url, fields=fields)
        return r.data
