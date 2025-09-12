import urllib3

class MyHTTPConnection:
    def __init__(self, host, port=None, timeout=None, source_address=None, blocksize=None):
        if ':' in host:
            host, port = host.split(':')
            port = int(port) if port.isdigit() else None

        self.host = host
        self.port = port if port else 80
        self.timeout = timeout
        self.source_address = source_address
        self.blocksize = blocksize

        self.http = urllib3.PoolManager(timeout=self.timeout)

    def make_request(self, path):
        url = f"http://{self.host}:{self.port}{path}"
        response = self.http.request('GET', url)
        return response.data

# Example usage
connection = MyHTTPConnection('example.com', timeout=5)
response_data = connection.make_request('/')
print(response_data)
