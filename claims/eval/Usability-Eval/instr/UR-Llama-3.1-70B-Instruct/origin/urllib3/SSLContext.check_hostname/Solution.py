import urllib3
import ssl

# Create a PoolManager with a custom SSL context
http = urllib3.PoolManager(
    ssl_context=ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH,
        cafile=None,
        capath=None,
        cadata=None
    )
)

# Enable hostname checking by setting server_hostname
http = urllib3.PoolManager(
    ssl_context=ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH,
        cafile=None,
        capath=None,
        cadata=None
    ),
    server_hostname='www.example.com'
)

# Alternatively, use PROTOCOL_TLS_CLIENT protocol which enables hostname checking by default
http = urllib3.PoolManager(
    ssl_version=ssl.PROTOCOL_TLS_CLIENT,
    server_hostname='www.example.com'
)

try:
    # Test the connection with hostname checking enabled
    resp = http.request('GET', 'https://www.example.com')
    print(resp.status)

except urllib3.exceptions.SSLError as e:
    print(f"SSL Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
