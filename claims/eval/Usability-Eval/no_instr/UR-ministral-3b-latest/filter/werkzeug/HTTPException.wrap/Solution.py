
from werkzeug.exceptions import HTTPException

class MyHTTPException(HTTPException):
    def __init__(self, message, status_code=500):
        super(MyHTTPException, self).__init__(message, status_code)

