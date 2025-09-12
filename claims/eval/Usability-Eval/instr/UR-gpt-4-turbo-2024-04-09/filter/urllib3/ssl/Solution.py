import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# Create a secure HTTPS connection pool manager
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Force certificate verification
    ca_certs=urllib3.util.ssl_.default_ssl_context().load_default_certs(),  # Use default system root CA certificates
    ssl_version=urllib3.util.ssl_.PROTOCOL_TLS,  # Use the best protocol that `ssl` supports
    ssl_context=create_urllib3_context()  # Create a custom SSL context
)

# URL you want to fetch securely
url = "https://example.com"

# Make a secure request to the server
try:
    response = http.request('GET', url)
    print('Status Code:', response.status)
    print('Headers:', response.headers)
    print('Body:', response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print('SSL/TLS security error:', e)
except urllib3.exceptions.HTTPError as e:
    print('HTTP error occurred:', e)

