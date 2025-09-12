# Importing required libraries
import urllib3
from urllib3.contrib import pyopenssl
import ssl
import socket

# Create a pool manager with pyOpenSSL support
http = urllib3.PoolManager(connection_timeout=5, num_pools=10, 
                          headers={"User-Agent": "Chrome/71.0.3578.98"},
                          chunked=True, retries=False, cert_reqs=ssl.CERT_REQUIRED, 
                          ssl_version=ssl.PROTOCOL_TLSv1_2, assert_fingerprint=False, timeout=urllib3.Timeout(sock_connect=5))

sock = socket.create_connection(('example.com', 443))
context = ssl.create_default_context()
with socket.create_connection(('example.com', 443)) as sock, context.wrap_socket(sock, server_hostname='example.com') as ssock:
    http.urlopen("GET", "https://example.com", headers={"User-Agent": "Chrome/71.0.3578.98"}, release_conn=False, retries=False, cert_reqs=ssl.CERT_REQUIRED, SSLContext=context)
