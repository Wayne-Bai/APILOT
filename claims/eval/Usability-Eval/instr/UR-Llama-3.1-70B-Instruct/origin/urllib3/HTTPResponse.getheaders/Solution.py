import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Define the URL for which you want to retrieve the headers
url = 'http://example.com'

# Send a HEAD request to the URL (HEAD request is similar to GET but it only returns the headers)
r = http.request('HEAD', url)

# Print the headers
for key, value in r.headers.items():
    print(f'{key}: {value}')
