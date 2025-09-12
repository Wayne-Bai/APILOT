from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, message, response=None, description=None, headers=None):
        super().__init__(message, response, description, headers)

raise CustomHTTPException("Custom Error Message", response="Custom Response", description="Custom Description", headers={"Custom-Header": "Custom Value"})
