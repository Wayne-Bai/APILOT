
import urllib3

class CustomHTTPConnection(urllib3.connection.HTTPConnection):
    def _read(self, amt=None, decode_content=None):
        data = super()._read(amt, decode_content)
        content_length = self.headers.get('Content-Length')
        if content_length is not None and len(data) != int(content_length):
            raise urllib3.exceptions.ContentLengthError("Content length does not match Content-Length header")
        return data

class CustomPoolManager(urllib3.PoolManager):
    def _new_pool(self, scheme, host, port, request_context=None):
        return CustomHTTPConnectionPool(host, port, **(self.connection_pool_kw))

http = CustomPoolManager()
