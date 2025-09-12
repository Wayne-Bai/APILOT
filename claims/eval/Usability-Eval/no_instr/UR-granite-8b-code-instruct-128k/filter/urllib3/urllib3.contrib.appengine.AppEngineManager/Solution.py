import urllib3

# Connection manager for Google App Engine sandbox applications.
class ConnectionManager:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def request(self, method, url, body=None, headers=None):
        if method == 'GET':
            return self.http.request('GET', url, body=body, headers=headers)
        elif method == 'POST':
            return self.http.request('POST', url, body=body, headers=headers)
        elif method == 'PUT':
            return self.http.request('PUT', url, body=body, headers=headers)
        elif method == 'DELETE':
            return self.http.request('DELETE', url, body=body, headers=headers)
        else:
            raise ValueError("Invalid method")
