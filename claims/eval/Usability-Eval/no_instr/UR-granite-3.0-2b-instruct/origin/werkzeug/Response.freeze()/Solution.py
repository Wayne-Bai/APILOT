from werkzeug.utils import secure_filename, median_abundance
from werkzeug.exceptions import HTTPException
from werkzeug.responses import Response, ResponseException

class PickleableResponse(Response):
    def prepare(self):
        self.data = [x for x in self.data]
        self.headers['Content-Length'] = str(len(self.data))
        if not hasattr(self, 'etag'):
            self.etag = secure_filename(self.content_type + '-' + hashlib.md5(self.data).hexdigest())
        super().prepare()

class PickleableResponseException(HTTPException):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.data = [x for x in self.data]
        self.headers['Content-Length'] = str(len(self.data))
        if not hasattr(self, 'etag'):
            self.etag = secure_filename(self.content_type + '-' + hashlib.md5(self.data).hexdigest())
