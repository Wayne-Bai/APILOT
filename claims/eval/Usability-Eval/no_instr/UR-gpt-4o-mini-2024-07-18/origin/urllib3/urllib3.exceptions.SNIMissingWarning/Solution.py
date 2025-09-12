import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(InsecureRequestWarning)

# Create a PoolManager instance
http = urllib3.PoolManager()

# Make an HTTPS request without SNI
url = "https://your-https-url.com/"

try:
    response = http.request('GET', url, assert_hostname=False)  # Disable SNI
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f'SSL Error: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
