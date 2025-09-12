import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the URL and port
url = 'https://example.com'

# Create an SSL context for the client
ssl_context = urllib3.util.ssl_.create_urllib3_context()

# Enable hostname checking explicitly
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Make a request using the SSL context with hostname verification enabled
try:
    response = http.request('GET', url, ssl_context=ssl_context)
    print("Response status:", response.status)
    print("Response data:", response.data.decode('utf-8'))

except Exception as e:
    print("An error occurred:", e)
