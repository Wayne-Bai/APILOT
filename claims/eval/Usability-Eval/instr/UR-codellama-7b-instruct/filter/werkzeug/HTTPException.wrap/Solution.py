
import werkzeug

class MyHTTPException(werkzeug.exceptions.HTTPException):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
