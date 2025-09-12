import urllib3
from urllib3.util import Retry

# Create a PoolManager instance to manage HTTP connections
http = urllib3.PoolManager()

# Specify the request URL and the HTTP method
host = 'http://httpbin.org'
path = '/get'
method = 'GET'

# Create a class to handle custom redirect logic
class CrossHostRedirectHandler(urllib3.RedirectHandler):
    def is_redirect_allowed(self, response, request_url, **kwargs):
        # Add custom logic here to allow cross-host redirects
        # For the purpose of this example, we'll allow any redirect
        return True

# Define custom Retry strategy
retries = Retry(
    total=3,  # Retry a total of 3 times
    backoff_factor=0.1,  # Backoff factor for delays between attempts
    status_forcelist=[500, 502, 503, 504],  # Retry on server errors
    redirect=2,  # Maximum number of redirects allowed
)

# Perform the request with the PoolManager
# Note that we only send the URI portion of the URL
response = http.request(
    method=method,
    url=path,
    retries=retries,
    redirect_handler=CrossHostRedirectHandler(),
    headers={"Host": "httpbin.org"},  # Manually add Host header
)

# Output the response details
print("Status Code:", response.status)
print("Response Body:", response.data.decode('utf-8'))

# Make sure to release the connection
response.release_conn()
