import urllib3

class GAEConnectionManager:
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get_request(self, url, headers=None):
        try:
            response = self.http.request('GET', url, headers=headers)
            return response.data.decode('utf-8')
        except urllib3.exceptions.HTTPError as e:
            return str(e)

    def post_request(self, url, data=None, headers=None):
        try:
            response = self.http.request('POST', url, body=data, headers=headers)
            return response.data.decode('utf-8')
        except urllib3.exceptions.HTTPError as e:
            return str(e)

# Example usage:
# manager = GAEConnectionManager()
# response = manager.get_request('https://example.com')
# print(response)
