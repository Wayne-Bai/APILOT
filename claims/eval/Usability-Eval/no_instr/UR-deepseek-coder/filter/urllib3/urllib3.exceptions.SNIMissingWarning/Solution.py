import urllib3

# Create a pool manager with SNI support
http = urllib3.PoolManager(assert_hostname=True)

try:
    # Make a HTTPS request
    response = http.request('GET', 'https://example.com')
    print(response.data.decode('utf-8'))
except urllib3.exceptions.SNIMissingWarning as e:
    # Warn if SNI is not available
    print("Warning: SNI is not available. Please ensure your environment supports SNI.")
    print(f"Details: {e}")
except urllib3.exceptions.HTTPError as e:
    print(f"An HTTP error occurred: {e}")
