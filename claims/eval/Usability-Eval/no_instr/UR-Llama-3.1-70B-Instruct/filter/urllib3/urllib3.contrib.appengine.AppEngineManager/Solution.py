import urllib3
from urllib3.contrib import pyopenssl
import ssl
import certifi

# Create a connection pool with the custom SSL context
class GAEConnectionManager:
    def __init__(self):
        # Create a custom SSL context
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        
        # Disable SSL verification for GAE development server
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

        # Create a connection pool with the custom SSL context
        self.http = pyopenssl.inject_into_urllib3()
        self.http.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.pool_manager = urllib3.PoolManager(
            ssl_context=self.ssl_context,
            num_pools=10,
            maxsize=10,
            block=True,
        )

    def get(self, url):
        return self.pool_manager.request('GET', url)

    def post(self, url, data=None, headers=None):
        return self.pool_manager.request('POST', url, body=data, headers=headers)

# Usage
if __name__ == "__main__":
    manager = GAEConnectionManager()
    response = manager.get('http://localhost:8080')

    print(response.status)
    print(response.data.decode('utf-8'))
