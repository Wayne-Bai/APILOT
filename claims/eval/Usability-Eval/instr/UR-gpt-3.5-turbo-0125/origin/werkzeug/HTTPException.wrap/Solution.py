
from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, exception_arg, description=None):
        super().__init__(description)
        self.exception_arg = exception_arg

    def __str__(self):
        return f'{self.exception_arg} - {self.description}'
