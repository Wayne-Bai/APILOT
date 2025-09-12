import urllib3
from OpenSSL import SSL
import socket

class TLSAdapter(urllib3.connectionpool.HTTPSConnectionPool):
    def __init__(self, *args, **kwargs):
        self.ssl_options = kwargs.pop('ssl_options', 0)
        super(TLSAdapter, self).__init__(*args, **kwargs)

    def _get_conn(self):
        conn = super(TLSAdapter, self)._get_conn()
        if not getattr(self, '_is_ssl', False):
            conn.sock = ssl_wrap_socket(conn.sock, self.ssl_options)
            self._is_ssl = True
        return conn

    def _new_conn(self):
        conn = super(TLSAdapter, self)._new_conn()
        if not getattr(self, '_is_ssl', False):
            conn.sock = ssl_wrap_socket(conn.sock, self.ssl_options)
            self._is_ssl = True
        return conn

def ssl_wrap_socket(sock, ssl_options):
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_options(ssl_options)
    connection = SSL.Connection(context, sock)
    return socket._fileobject(_sock=connection)

# Usage:
http = urllib3.PoolManager()
adapter = TLSAdapter(host='example.com', port=443)
r = adapter.request('GET', '/')
