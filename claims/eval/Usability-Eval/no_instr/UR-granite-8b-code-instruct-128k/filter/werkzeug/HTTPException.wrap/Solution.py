from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, message, response_code=500):
        super().__init__(message)
        self.response_code = response_code
