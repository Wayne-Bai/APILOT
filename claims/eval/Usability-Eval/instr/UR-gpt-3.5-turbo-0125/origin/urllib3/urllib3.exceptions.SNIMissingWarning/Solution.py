
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

# Send an HTTPS request without SNI
try:
    http.request('GET', 'https://example.com', assert_same_host=False)
except urllib3.exceptions.SNIMissingWarning as e:
    print('Warning:', e)
