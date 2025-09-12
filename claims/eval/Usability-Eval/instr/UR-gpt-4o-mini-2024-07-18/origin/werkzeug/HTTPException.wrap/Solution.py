from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)

# Usage example
try:
    raise CustomHTTPException("This is a custom exception message", response="Custom Response")
except CustomHTTPException as e:
    print(f"Exception raised: {e.description}")
    print(f"Response: {e.get_response()}")
