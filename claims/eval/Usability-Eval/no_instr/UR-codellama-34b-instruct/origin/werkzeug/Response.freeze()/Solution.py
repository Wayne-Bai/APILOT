import werkzeug.wrappers
from werkzeug.wrappers import BaseResponse as Response

class PicklableResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicit_sequence_conversion = False
        self.direct_passthrough = False
        self._buffer = []

    def buffer(self, data):
        if self.implicit_sequence_conversion and isinstance(data, (list, tuple)):
            for item in data:
                self._buffer.append(item)
        else:
            self._buffer.append(data)

    def get_content_length(self):
        if self._headers.get('Content-Length'):
            return int(self._headers['Content-Length'])
        return 0

    def set_etag(self, etag):
        if not self._headers.get('ETag'):
            self._headers['ETag'] = '"{}"'.format(etag)
