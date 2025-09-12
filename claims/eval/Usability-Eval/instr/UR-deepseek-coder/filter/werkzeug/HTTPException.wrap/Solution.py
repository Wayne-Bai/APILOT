from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
