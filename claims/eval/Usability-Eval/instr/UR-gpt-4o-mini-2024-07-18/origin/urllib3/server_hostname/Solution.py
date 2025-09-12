import urllib3

class CustomHTTPClient:
    def __init__(self, hostname=None):
        self.hostname = hostname
        self.http = urllib3.PoolManager()

    def get_hostname(self):
        return self.hostname

    def make_request(self, path):
        if self.hostname is None:
            raise ValueError("Hostname is not specified.")
        
        url = f"http://{self.hostname}/{path}"
        response = self.http.request('GET', url)
        return response.data

# Example usage
client = CustomHTTPClient('example.com')
print(client.get_hostname())  # Outputs: example.com
response_data = client.make_request('path/to/resource')
print(response_data)
