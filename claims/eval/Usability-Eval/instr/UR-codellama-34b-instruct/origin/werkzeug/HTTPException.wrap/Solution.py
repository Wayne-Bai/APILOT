
from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

    def get_response(self):
        response = super().get_response()
        if self.error_code is not None:
            response.status_code = self.error_code
        return response
