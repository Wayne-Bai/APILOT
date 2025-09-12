from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, message, status_code):
        super().__init__(description=message, response=None)
        self.code = status_code

# Example usage
try:
    raise CustomHTTPException("This is a custom error message.", 400)
except CustomHTTPException as e:
    print(f"Error occurred: {e.description} with status code {e.code}")
