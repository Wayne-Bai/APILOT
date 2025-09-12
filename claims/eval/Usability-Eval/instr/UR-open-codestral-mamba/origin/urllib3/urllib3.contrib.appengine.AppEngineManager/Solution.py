import urllib3

class ConnectionManager:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get_request(self, url):
        response = self.http.request('GET', url)
        return response.data

    def post_request(self, url, data):
        response = self.http.request('POST', url, fields=data)
        return response.data

    def close_pool(self):
        self.http.close()
