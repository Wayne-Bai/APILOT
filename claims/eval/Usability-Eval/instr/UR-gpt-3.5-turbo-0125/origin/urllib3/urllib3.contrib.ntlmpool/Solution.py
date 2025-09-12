
import urllib3
from requests_ntlm import HttpNtlmAuth

pool = urllib3.PoolManager()
url = 'https://example.com/api/data'
r = pool.request('GET', url, headers={'Accept': 'application/json'}, auth=HttpNtlmAuth('domain\\username', 'password'))

print(r.status)
print(r.data)
