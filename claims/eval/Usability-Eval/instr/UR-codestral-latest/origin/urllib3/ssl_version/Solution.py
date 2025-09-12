import urllib3

# Disable warnings for insecure SSL requests (use with caution)
urllib3.disable_warnings()

# Create a pool manager with the specified SSL version. Here, SSL version 3 is used.
http = urllib3.PoolManager(
    ssl_version=urllib3.util.ssl_.PROTOCOL_SSLv3
)

# Make a GET request to the specified URL
response = http.request('GET', 'https://example.com')

# Print the status of the response
print(response.status)
