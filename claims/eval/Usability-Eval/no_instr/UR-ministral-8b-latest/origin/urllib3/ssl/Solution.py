import urllib3

# Enable warning for SSL certificate errors which can be ignored in some cases with standards
import urllib3.exceptions
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a client instance
http = urllib3.PoolManager()

# This is an example of a simple GET request to a HTTPS URL
url = 'https://example.com'
response = http.request('GET', url, cert_reqs='CERT_NONE', ssl_version=None)  # SSL version can be None, PROTOCOL_TLS, etc.

# Print the response
print(response.data)
