import urllib3

class ConnectionManager:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get(self, url):
        response = self.http.request('GET', url)
        return response.data

    def post(self, url, data):
        response = self.http.request('POST', url, fields=data)
        return response.data

# Example usage
if __name__ == "__main__":
    conn_manager = ConnectionManager()
    url = 'https://httpbin.org/get'
    print(conn_manager.get(url))

    data = {'key': 'value'}
    url = 'https://httpbin.org/post'
    print(conn_manager.post(url, data))
