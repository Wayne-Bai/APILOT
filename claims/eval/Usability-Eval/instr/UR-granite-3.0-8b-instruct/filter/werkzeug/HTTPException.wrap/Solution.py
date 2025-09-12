from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description, status_code=400):
        super().__init__(description, status_code)
