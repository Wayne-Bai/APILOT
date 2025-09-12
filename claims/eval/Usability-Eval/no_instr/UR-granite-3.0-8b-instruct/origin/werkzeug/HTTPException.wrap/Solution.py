from werkzeug.exceptions import HTTPException

class CustomException(HTTPException):
    def __init__(self, exception):
        super().__init__()
        self.exception = exception
