import urllib3
from requests_ntlm import HttpNtlmAuth
from urllib3.util import Retry
from urllib3.poolmanager import PoolManager

class NTLMHttpPool(PoolManager):
    def __init__(self, username, password, *args, **kwargs):
        super(NTLMHttpPool, self).__init__(*args, **kwargs)

        self.auth = HttpNtlmAuth(username, password)

    def urlopen(self, method, url, redirect=True, retries=Retry.DEFAULT, *args, **kwargs):
        """
        Same as HTTPConnectionPool.urlopen() but with NTLM authentication headers
        """
        headers = kwargs.pop('headers', {})
        headers.update(urllib3.make_headers(proxy_basic_auth=self.auth))
        
        return super(NTLMHttpPool, self).urlopen(method, url, redirect=redirect, retries=retries, headers=headers, *args, **kwargs)


# Usage
username = 'your_username'
password = 'your_password'
url = 'http://example.com/protected_page'

# Create a pool with NTLM authentication
http_pool = NTLMHttpPool(username, password)

# Send a request to the server
response = http_pool.urlopen('GET', url)
print(response.data.decode('utf-8'))
