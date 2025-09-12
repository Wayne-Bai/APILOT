# Importing Werkzeug exceptions
from werkzeug.exceptions import HTTPException

class CustomInternalServerError(HTTPException):
    """A custom 500 Internal Server Error Exception"""
    code = 500
    description = "Internal Server Error"
    name = "InternalServerError"

    def __init__(self, exception=None):
        """Initialize the exception with the given exception"""
        super().__init__("Server error, please check the server logs.")
        self.exception = exception
