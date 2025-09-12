from werkzeug.wrappers import Response
from werkzeug.wsgi import wrap_file
import pickle

class BufferedResponse(Response):
    def __init__(self, response=None, etag=None, status=200, headers=None,
                 content_type='text/html', direct_passthrough=False,
                 implicitly_sequence_conversion=False):
        super(BufferedResponse, self).__init__(response, status=status, headers=headers, content_type=content_type)
        self.direct_passthrough = direct_passthrough
        self.implicitly_sequence_conversion = implicitly_sequence_conversion
        if self.direct_passthrough:
            self.cache_control.no_cache = True
        self.set_etag(etag)

        # Ensure the Content-Length header is set, since WSGI does not want to do it.
        # Note that it's amost always incorrect to set the Content-Length in WSGI, it's up to the server.
        if 'Content-Length' not in self.headers:
            if hasattr(self.response, '__len__'):
                self.headers['Content-Length'] = str(len(self.response))
            else:
                # The WSGI specification requires the Content-Length header to be here.
                self.headers['Content-Length'] = '0'

    def write_to_sequence(self):
        """Casts the response content to string iterable (string list). This requires the response type of sequence,
           None, bytes, string or a Werkzeug WSGI wrapper. It uses the wsgi_file_wrapper to prevent Python from creating
           the full non-bufferable list.
        ::
        """
        if self.is_sequence or self.direct_passthrough or self.response is None:
            return self
        rv = self.response
        if hasattr(rv, 'seek'):
            rv.seek(0)
            return self.wrap(wrap_file(self.environ, rv))
        if isinstance(rv, (list, tuple)):
            return self.wrap(rv)
        if isinstance(rv, bytes) or isinstance(rv, str):
            return self.wrap_bytes(rv)
        if hasattr(rv, 'read'):
            rv = wrap_file(self.environ, rv)
            return self.wrap(rv)
        total_len = 0

        try:
            it = iter(rv)
            rv = [None] * len(rv)
        except (TypeError, AttributeError):
            return self.wrap_no_sequence(rv)

        for n, item in enumerate(it):
            item = self.write_to_sequence(item)
            total_len += len(item)
            rv[n] = item

        if total_len != int(self.headers.get('Content-Length', 0)):
            raise RuntimeError(f'Wrong sequence length, expected {total_len}, got {len(rv)}.')
        return rv

    def make_conditional(self, stat):
        return self

    def set_etag(self, etag):
        if self.headers.get('ETag') is None:
            self.headers['ETag'] = etag

pickled_response = pickle.dumps(BufferedResponse(response={"result": "success"}))

print(pickled_response)
