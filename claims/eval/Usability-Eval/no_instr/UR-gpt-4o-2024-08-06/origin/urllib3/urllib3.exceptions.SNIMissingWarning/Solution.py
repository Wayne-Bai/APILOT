import urllib3
import warnings

# Suppress warnings about making an HTTPS request without SNI
warnings.filterwarnings('default', category=urllib3.exceptions.SubjectAltNameWarning)

# Create a PoolManager, because it handles connections for us
http = urllib3.PoolManager()

# Example of making a HTTPS request to a URL
url = 'https://example.com/'
try:
    response = http.request('GET', url)
    print(response.status)
    print(response.data.decode('utf-8'))

except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
