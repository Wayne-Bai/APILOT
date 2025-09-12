
import urllib3

# Create a PoolManager instance
pool = urllib3.PoolManager()

# Define the URL
url = 'http://example.com'

# Make the request
r = pool.request('GET', url)

# Check the status code
if r.status == 200:
    # Do something with the response
    print(r.data)
else:
    # Handle the error
    print('Request failed with status code:', r.status)
