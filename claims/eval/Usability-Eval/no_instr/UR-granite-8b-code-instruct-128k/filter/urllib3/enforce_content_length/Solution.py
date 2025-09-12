import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Enforce content length checking
def enforce_content_length(response):
    content_length = response.headers.get('Content-Length')
    if content_length and len(response.data) != int(content_length):
        raise ValueError('Content length mismatch')

# Make a request
response = http.request('GET', 'http://example.com')

# Enforce content length checking
enforce_content_length(response)
