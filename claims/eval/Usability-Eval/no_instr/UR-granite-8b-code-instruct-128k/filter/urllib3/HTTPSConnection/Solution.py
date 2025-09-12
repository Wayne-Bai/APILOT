import urllib3

from urllib3.contrib import pyopenssl
from urllib3.poolmanager import HTTPConnectionPool, HTTPSConnectionPool
from urllib3.response import HTTPResponse
from urllib3.exceptions import InsecureRequestWarning
from urllib3.connection import HTTPConnection, HTTPSConnection

urllib3.disable_warnings(InsecureRequestWarning)

class HTTPSConnectionPool(HTTPSConnectionPool):
    def __init__(self,
                 host='localhost',
                 port=None,
                 *,
                 strict=None,
                 timeout=None,
                 maxsize=None,
                 block=False,
                 headers=None,
                 assert_hostname=None,
                 ssl_version=None,
                 ca_certs=None,
                 ca_cert_dir=None,
                 cert_reqs=None,
                 ssl_context=None):
        if strict is not None:
            assert isinstance(strict, bool), \
                'strict must be a boolean value'
        if cert_reqs is not None:
            assert cert_reqs in (ssl.CERT_NONE, ssl.CERT_OPTIONAL, ssl.CERT_REQUIRED), \
                'cert_reqs must be one of ssl.CERT_NONE, ssl.CERT_OPTIONAL, ssl.CERT_REQUIRED'
        if not isinstance(ssl_version, int):
            raise ValueError('ssl_version must be an integer value, e.g. ssl.PROTOCOL_TLSv1')
        if ssl_context is not None:
            assert isinstance(ssl_context, ssl.SSLContext), \
                'ssl_context must be an ssl.SSLContext instance'

        if assert_hostname is None:
            assert_hostname = strict

        if ssl_version is None:
            ssl_version = ssl.PROTOCOL_TLSv1

        super().__init__(
            host=host,
            port=port,
            strict=strict,
            timeout=timeout,
            maxsize=maxsize,
            block=block,
            headers=headers,
        )

        self.assert_hostname = assert_hostname
        self.ssl_version = ssl_version
        self.ca_certs = ca_certs
        self.ca_cert_dir = ca_cert_dir
        self.cert_reqs = cert_reqs
        self.ssl_context = ssl_context