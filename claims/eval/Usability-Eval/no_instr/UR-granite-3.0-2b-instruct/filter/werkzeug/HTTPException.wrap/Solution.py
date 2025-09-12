from werkzeug.exceptions import HTTPException

class CustomException(HTTPException):
    def __init__(self, message, status_code):
        super().__init__(message, status_code)
