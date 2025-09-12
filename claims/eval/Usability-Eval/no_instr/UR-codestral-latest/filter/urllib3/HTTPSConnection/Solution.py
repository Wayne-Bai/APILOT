import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_

class SSLContextAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl_.create_urllib3_context()
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl_.PROTOCOL_TLSv1_2,
                                       ssl_context=ctx)

session = requests.Session()
session.mount('https://', SSLContextAdapter())

response = session.get('https://secure_server')

print(response.text)
