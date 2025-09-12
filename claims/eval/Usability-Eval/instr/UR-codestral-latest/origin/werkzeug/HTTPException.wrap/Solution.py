from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, message):
        super().__init__()
        self.description = message

# Usage
# Raise the exception with a custom message
raise CustomHTTPException("This is a custom HTTP exception")
