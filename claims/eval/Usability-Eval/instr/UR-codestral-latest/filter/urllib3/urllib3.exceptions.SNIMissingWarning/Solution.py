import urllib3
from urllib3.exceptions import SNIMissingWarning
import warnings

# Disable the SNIMissingWarning warning
warnings.filterwarnings("ignore", category=SNIMissingWarning)

# Set up the HTTPS connection pool
http = urllib3.PoolManager()

# Make the HTTPS request
response = http.request('GET', 'https://example.com')
