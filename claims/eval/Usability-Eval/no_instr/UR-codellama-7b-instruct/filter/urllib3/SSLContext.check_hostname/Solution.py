
from urllib3 import ProxyManager, TCPTimeout
import ssl

proxy = "your-proxy"

manager = ProxyManager(
    proxy,
    cert_reqs="CERT_REQUIRED",
    ca_certs="path/to/cacert.pem",
    scheme="https"
)

tcp_timeout = TCPTimeout()

with manager.wrap_socket(ssl.SSLSocket, server_hostname="your-domain.com") as conn:
    conn.do_handshake()
