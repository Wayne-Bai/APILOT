import urllib3

class SSLHTTPConnection(urllib3.connectionpool.HTTPConnection):
    def __init__(self, host, port=443, **kwargs):
        super(SSLHTTPConnection, self).__init__(host, port, **kwargs)
        self.poolmanager = urllib3.poolmanager.PoolManager(ssl_version=3)

    def _new_conn(self):
        conn = self.poolmanager.connection_from_url(self.scheme + "://" + self.host)
        return conn

    def _prepare_conn(self, conn):
        conn.sock = self.sock
        conn._prepare_proxy(self)

    def _send_request(self, conn, method, url, body, headers):
        conn.request(method, url, body, headers)

    def _get_response(self, conn):
        return conn.getresponse()
