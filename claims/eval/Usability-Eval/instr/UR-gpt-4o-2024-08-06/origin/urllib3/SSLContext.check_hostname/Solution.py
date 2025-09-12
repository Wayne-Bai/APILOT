import urllib3
from urllib3.util.ssl_ import create_urllib3_context, DEFAULT_CIPHERS

# Create a custom SSL context with hostname checking enabled
ssl_context = create_urllib3_context()
ssl_context.verify_mode = urllib3.util.ssl_.CERT_REQUIRED  # Enforce certificate requirement
ssl_context.check_hostname = True  # Enable hostname checking

# Create a PoolManager using the custom SSL context
http = urllib3.PoolManager(ssl_context=ssl_context)

# Make a request to a secure site (example using https://www.example.com)
try:
    response = http.request('GET', 'https://www.example.com')
    print(response.status)  # Print the HTTP status code
    print(response.data.decode('utf-8'))  # Decode and print the response data
except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except Exception as e:
    print(f"Error: {e}")
