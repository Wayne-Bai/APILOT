import urllib3

# Create a pool manager with a custom warning filter
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=urllib3.util.DEFAULT_CA_BUNDLE_PATH,
    assert_hostname=False
)

# Function to make a HTTPS request and handle warnings
def make_https_request(url):
    try:
        response = http.request('GET', url)
        print(f"Response status: {response.status}")
        print(f"Response data: {response.data}")
    except urllib3.exceptions.SNIMissingWarning as e:
        print("Warning: SNI (Server Name Indication) is not available.")
        print(f"Error details: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
make_https_request("https://example.com")
