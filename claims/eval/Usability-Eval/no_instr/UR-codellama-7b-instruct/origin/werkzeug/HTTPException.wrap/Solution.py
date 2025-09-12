
from werkzeug import exceptions

class MyException(exceptions.HTTPException):
    def __init__(self, message):
        super().__init__(message)
