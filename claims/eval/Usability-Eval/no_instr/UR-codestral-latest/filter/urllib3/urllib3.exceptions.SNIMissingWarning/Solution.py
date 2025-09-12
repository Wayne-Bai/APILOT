import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(InsecureRequestWarning)

http = urllib3.PoolManager()

# Make a request without checking the certificate
response = http.request('GET', 'https://example.com', verify=False)
