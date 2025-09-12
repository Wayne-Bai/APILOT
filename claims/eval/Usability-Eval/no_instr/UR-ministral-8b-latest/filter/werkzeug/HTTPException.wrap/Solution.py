from werkzeug.exceptions import HTTPException

class CustomHTTPError(HTTPException):
    def __init__(self, description, status_code):
        super().__init__(description=description, status_code=status_code)

# Example usage
def get_custom_error():
    raise CustomHTTPError("This is a custom error", 418)

try:
    get_custom_error()
except CustomHTTPError as e:
    # Handle the custom exception
    print(f"Caught an error: {e.description} with status code {e.status_code}")
