from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description):
        self.description = description
        super().__init__(description)
