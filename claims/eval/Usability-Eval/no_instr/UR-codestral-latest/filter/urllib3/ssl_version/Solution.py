import urllib3
import ssl

ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT for SSL v3 or OP_NO_TLSv1_2 for disabling TLS 1.2

http = urllib3.PoolManager(
    ssl_context=ctx,
    # other arguments for the PoolManager constructor if needed
)

# Now you can use the 'http' object to make requests, e.g.
response = http.request('GET', 'https://example.com')
