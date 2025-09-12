from urllib3.poolmanager import PoolManager
import urllib3
import urllib.parse

class CustomManager:
    def __init__(self):
        self.pool_manager = PoolManager(num_pools=10)

    def request(self, method, url, *args, **kwargs):
        # Fetch and unquote the URL
        url_parts = urllib.parse.urlparse(url)
        encoded_parts = urllib.parse.parse_qs(url_parts.query)
        
        for key, values in encoded_parts.items():
            encoded_parts[key] = values[0]
        
        # Since the original URL includes query string parameters, we need to encode these back into the URL
        query_string = urllib.parse.urlencode(encoded_parts)
        # Construct the new URL with the parameters
        new_url = f"{url_parts.scheme}://{url_parts.netloc}{url_parts.path}?{query_string}"
        
        # Send the request using the custom PoolManager
        return self.pool_manager.request(method, new_url, *args, **kwargs)

# Example Usage
manager = CustomManager()
response = manager.request('GET', 'http://domain.org')
print(response.status)
