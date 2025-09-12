import urllib3

class ConnectionManager:
    def __init__(self):
        # Create a PoolManager instance to manage connections.
        self.http = urllib3.PoolManager()

    def get(self, url, params=None):
        response = self.http.request('GET', url, fields=params)
        return response.data.decode('utf-8')

    def post(self, url, data=None):
        response = self.http.request('POST', url, fields=data)
        return response.data.decode('utf-8')

# Example usage:
if __name__ == "__main__":
    manager = ConnectionManager()
    get_response = manager.get('https://jsonplaceholder.typicode.com/posts')
    print(get_response)

    post_response = manager.post('https://jsonplaceholder.typicode.com/posts', 
                                  data={'title': 'foo', 'body': 'bar', 'userId': 1})
    print(post_response)
