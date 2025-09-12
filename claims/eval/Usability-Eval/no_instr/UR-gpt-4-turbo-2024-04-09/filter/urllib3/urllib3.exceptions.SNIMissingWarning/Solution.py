import urllib3
import warnings
from urllib3.util import SSLContext
from urllib3.exceptions import SNIMissingWarning

def check_sni_support():
    context = SSLContext()
    if not hasattr(context, 'sni'):
        warnings.warn(
            "SNI (Server Name Indication) is not supported by your platform. "
            "Some HTTPS requests might fail.", SNIMissingWarning)

# Configure urllib3 to use a PoolManager
http = urllib3.PoolManager()

# Perform the SNI check
check_sni_support()

# Example request
try:
    response = http.request('GET', 'https://example.com')
    print(response.status)
    print(response.data)
except urllib3.exceptions.SSLError as e:
    print(f"SSL error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
