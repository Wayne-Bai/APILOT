import urllib3

http = urllib3.PoolManager(
ssl_version=urllib3.protocol.SSLContext(ssl.PROTOCOL_TLS)
)
