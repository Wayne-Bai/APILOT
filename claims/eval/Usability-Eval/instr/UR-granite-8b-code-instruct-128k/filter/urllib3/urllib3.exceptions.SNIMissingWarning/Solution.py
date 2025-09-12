import urllib3

# Create an HTTPS connection pool
https_pool = urllib3.PoolManager()

# Make a request to a HTTPS server without SNI
try:
    response = https_pool.request('GET', 'https://example.com')
except urllib3.exceptions.SNIMissingWarning as e:
    print(f'Warning: {e}')
