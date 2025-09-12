import urllib3

class ConnectionManager:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def send_request(self, method, url, **kwargs):
        response = self.http.request(method, url, **kwargs)
        return response
