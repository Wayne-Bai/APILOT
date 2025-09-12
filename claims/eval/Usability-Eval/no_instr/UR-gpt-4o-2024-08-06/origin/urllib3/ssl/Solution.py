import urllib3

# Initialize a PoolManager instance with TLS settings
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Require certificate verification
    ca_certs=urllib3.util.ssl_.DEFAULT_CA_BUNDLE_PATH  # Path to default CA bundle
)

# Example of making a secure HTTP request
url = 'https://www.example.com'

try:
    response = http.request('GET', url)
    print(f"Response Status: {response.status}")
    print("Response Data:")
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except urllib3.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

# Release the connection
http.clear()
