import urllib3
import warnings

# Enable logging to track HTTPS request
urllib3.util.log.setLevel('DEBUG')

# Enable warnings to track HTTPS request without SNI
warnings.simplefilter('always', urllib3.exceptions.InsecureRequestWarning)

# Create a pool manager
http = urllib3.PoolManager()

# Make a request to a server that doesn't support SNI (Server Name Indication)
try:
    response = http.request('GET', 'https://www.stunnel.org:10421')
except urllib3.exceptions.InsecureRequestWarning as e:
    print(f'SNI not available. Error: {e}')
except urllib3.exceptions.SSLError as e:
    print(f'SSL/TLS verification failed. Error: {e}')
