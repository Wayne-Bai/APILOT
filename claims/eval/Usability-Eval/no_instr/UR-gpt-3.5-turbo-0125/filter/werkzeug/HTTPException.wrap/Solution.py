
from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, exception_arg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exception_arg = exception_arg
