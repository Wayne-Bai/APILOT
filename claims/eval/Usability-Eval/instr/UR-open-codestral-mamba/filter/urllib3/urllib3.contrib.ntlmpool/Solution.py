import urllib3
import requests
from requests_ntlm import HttpNtlmAuth

def get_pool_with_ntlm_auth(url, username, password):
    """
    Returns a urllib3 connection pool that allows pooling connections with NTLM authentication
    """

    class NTLMHttpAdapter(requests.adapters.HTTPAdapter):
        def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
            if request.url.startswith('https'):
                v = requests.packages.urllib3.util.parse_url(request.url)
                v = (username, password, url.hostname, url.port)
                request.url = request.url.replace(v[2], ':'.join(map(str, v[3:])))

            return super(NTLMHttpAdapter, self).send(request, stream, timeout, verify, cert, proxies)

    s = requests.Session()
    s.mount(url, NTLMHttpAdapter())

    # Simulate some API calls using the Pool object
    http = urllib3.PoolManager()

    r = http.request('GET', url)
    print(r.status)
    print(r.data)
    return http

# Replace 'url', 'username', and 'password' with your actual values
url = 'https://example.com'
username = 'my_username'
password = 'my_password'

get_pool_with_ntlm_auth(url, username, password)
