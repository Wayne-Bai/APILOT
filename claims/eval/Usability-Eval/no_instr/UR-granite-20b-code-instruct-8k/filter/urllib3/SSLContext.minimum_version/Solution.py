
from urllib3 import PoolManager

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2
http = PoolManager(ssl_context=ssl_context)
