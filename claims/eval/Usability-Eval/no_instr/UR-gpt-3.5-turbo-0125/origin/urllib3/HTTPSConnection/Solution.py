
import urllib3
import ssl

class MyHTTPSConnection(urllib3.connection.HTTPSConnection):
    default_port = 443

    def __init__(self, host, port=None, key_file=None, cert_file=None, strict=None,
                 timeout=urllib3.connection.DEFAULT_TIMEOUT, maxsize=urllib3.connection.DEFAULT_MAXSIZE,
                 block=urllib3.connection.DEFAULT_BLOCK_SIZE, headers=None, context=None):

        ssl_context = ssl.create_default_context() if context is None else context
        super().__init__(host, port, timeout=timeout, maxsize=maxsize, block=block,
                         headers=headers, key_file=key_file, cert_file=cert_file,
                         strict=strict, context=ssl_context)
