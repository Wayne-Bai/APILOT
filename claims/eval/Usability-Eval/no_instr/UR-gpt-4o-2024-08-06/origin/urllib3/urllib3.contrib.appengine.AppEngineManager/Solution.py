import urllib3

class ConnectionManager:
    def __init__(self):
        # Create a PoolManager instance to make requests.
        self.http = urllib3.PoolManager()

    def fetch_url(self, url):
        """
        Fetches content from a given URL.

        :param url: URL to fetch data from
        :return: Response data from the URL
        """
        try:
            response = self.http.request('GET', url)
            
            if response.status == 200:
                return response.data
            else:
                return f"Failed to fetch {url}, status code: {response.status}"
        
        except Exception as e:
            return f"An error occurred: {e}"

    def close_connections(self):
        """
        Close connections in the pool.
        """
        self.http.clear()

# Usage example:
if __name__ == "__main__":
    manager = ConnectionManager()
    url = 'http://www.example.com'
    
    content = manager.fetch_url(url)
    print(content)
    
    # Clean up
    manager.close_connections()
