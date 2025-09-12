import urllib3

class HTTPSConnection(urllib3.HTTPConnection):
    """
    A subclass of HTTPConnection that uses SSL for communication with secure servers.
    Default port is 443. If context is specified, it must be a ssl.SSLContext instance
    describing the various SSL options.
    """
    default_port = 443

    def __init__(self, host, port=None, strict=None, timeout=None, proxy_info=None, num_pools=10, headers=None, max_retries=0, encoded_host=None, pool_connections=None, connection_kw=None, context=None):
        super().__init__(host, port, strict, timeout, proxy_info, num_pools, headers, max_retries, encoded_host, pool_connections, connection_kw)
        self.context = context
