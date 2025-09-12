from werkzeug.exceptions import HTTPException

class MyHTTPException(HTTPException):
    def __init__(self, message, status_code=None):
        self.message = message
        if not status_code:
            status_code = 500
        self.status_code = status_code
        super().__init__(self.message)
