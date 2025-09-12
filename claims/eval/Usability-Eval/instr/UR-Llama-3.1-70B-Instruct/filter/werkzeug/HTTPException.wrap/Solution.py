# Importing the required module from werkzeug
from werkzeug.exceptions import HTTPException

# Creating a custom exception that is a subclass of the calling HTTP exception and the exception argument
class CustomHTTPException(Exception):
    def __init__(self, exception, http_exception, *args, **kwargs):
        self.exception = exception
        self.http_exception = http_exception
        super().__init__(*args, **kwargs)

# Creating a custom exception that is a subclass of both the calling HTTP exception and the exception argument
class CustomInternalServerError(Exception, HTTPException):
    code = 500
    description = 'Internal Server Error'

    def __init__(self, original_exception, *args, **kwargs):
        self.original_exception = original_exception
        super().__init__(*args, **kwargs)

# Example usage
try:
    raise CustomHTTPException(Exception('Original Exception'), HTTPException('HTTP Exception'))
except CustomHTTPException as e:
    print(f"Original Exception: {e.exception}")
    print(f"HTTP Exception: {e.http_exception}")

try:
    raise CustomInternalServerError(Exception('Original Exception'))
except CustomInternalServerError as e:
    print(f"Status Code: {e.code}")
    print(f"Description: {e.description}")
    print(f"Original Exception: {e.original_exception}")
