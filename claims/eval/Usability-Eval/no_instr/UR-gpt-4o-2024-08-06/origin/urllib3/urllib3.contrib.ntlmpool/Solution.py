import urllib3
from requests_ntlm import HttpNtlmAuth

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the NTLM authenticated pool manager
class NTLMAuthPoolManager(urllib3.PoolManager):
    def __init__(self, username, password, *args, **kwargs):
        kwargs['cert_reqs'] = 'CERT_NONE'
        self.auth = HttpNtlmAuth(username, password)
        super().__init__(*args, **kwargs)

    def urlopen(self, method, url, redirect=True, **kw):
        kw['headers'] = urllib3.util.make_headers(keep_alive=True, basic_auth=self.auth.credentials)
        response = super().urlopen(method, url, redirect=redirect, **kw)
        response.authenticate = self.auth
        return response

# Usage
if __name__ == '__main__':
    # Replace with your username and password
    username = 'DOMAIN\\username'
    password = 'password'

    http = NTLMAuthPoolManager(username=username, password=password)
    url = 'http://example.com'
    response = http.request('GET', url)

    print(response.status)
    print(response.data)
