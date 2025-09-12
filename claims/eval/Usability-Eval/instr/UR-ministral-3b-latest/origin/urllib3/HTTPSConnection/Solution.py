from urllib3.connection import HTTPConnection
from urllib3.poolmanager import PoolManager
from urllib3.util.ssl_ import default_import_path
import ssl

class SecureHTTPConnection(HTTPConnection):
    def __init__(self, host, *args, **kwargs):
        super(SecureHTTPConnection, self).__init__(host, *args, **kwargs)
        self.default_port = 443 # Default port for secure servers
        self.timeout = kwargs.get('timeout', 50)

    def _make_request(self, method, req, **kwargs):
        with PoolManager() as pool:
            secure_query = {
                "method": method,
                "url": req.url,
                "headers": req.headers,
                "body": req.data,
                "decode_content": req.decode_content,
                "cert_reqs": ssl.CERT_NONE # If SSL context provided by user, then TLS certificate verification is handled by SSL context
            }

            self._pre_setup(secure_query, host=req.url)
            if "cert" in secure_query:
                secure_query["ssl_context"] = secure_query["cert"]

            self._conn = poolParams[req.url]
            self._conn.set_timeouts(
                read=self.timeout,
                write=self.timeout
            )
            return self._conn.request(req, **secure_query)

# Example usage
conn = SecureHTTPConnection('www.google.com', socket=MySocketWrapper)
r = conn.request(method='GET')
