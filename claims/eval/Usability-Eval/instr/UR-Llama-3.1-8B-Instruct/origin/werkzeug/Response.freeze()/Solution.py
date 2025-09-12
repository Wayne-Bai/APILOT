from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.wrappers import Response
from werkzeug.utils import cached_property

class WSGIResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response_buffer = []

    def set_cookie(self, *args, **kwargs):
        cookie = super().set_cookie(*args, **kwargs)
        self.response_buffer.append(cookie)
        return cookie

    @cached_property
    def etag(self):
        if 'ETag' in self.headers:
            return self.headers['ETag']
        return '{%s}' % id(self)

    def flush(self):
        content = '\r\n'.join(self.response_buffer)
        self.response_buffer = []
        self.set_header('Content-Length', str(len(content)))
        super().close = lambda: None
        super().etags = lambda: None

# Usage example:
response = WSGIResponse('Hello, World!')
response.set_header('Content-Type', 'text/plain')
response.set_cookie('session', '12345')

response.flush()

print(response)
