
from werkzeug.exceptions import HTTPException

class CustomException(HTTPException):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
