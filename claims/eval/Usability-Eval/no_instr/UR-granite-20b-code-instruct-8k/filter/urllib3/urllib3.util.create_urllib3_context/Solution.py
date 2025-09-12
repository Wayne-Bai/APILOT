import urllib3

ssl_context = urllib3.util.ssl_wrap_socket.ssl_wrap_socket(
ca_certs=None,
cert_reqs=None,
ssl_version=ssl.PROTOCOL_TLS,
ciphers=None,
keyfile=None,
certfile=None,
)
