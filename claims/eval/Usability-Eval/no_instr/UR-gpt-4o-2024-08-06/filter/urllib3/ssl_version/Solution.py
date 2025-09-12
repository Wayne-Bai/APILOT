import urllib3

# Create a PoolManager with custom SSL configurations
http = urllib3.PoolManager(
    ssl_version=urllib3.util.ssl_.PROTOCOL_TLSv1_2, # Example of setting a minimum SSL version to TLSv1.2
)

# Define the server URL
url = "https://example.com"

# Make a request to the server
try:
    response = http.request('GET', url)
    # Print the response from the server
    print(f"Status code: {response.status}")
    print(f"Response data: {response.data.decode('utf-8')}")
except urllib3.exceptions.SSLError as e:
    print(f"SSL error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
