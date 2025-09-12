from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)

# Example of raising the custom exception with a specific description
try:
    raise CustomHTTPException(description="This is a custom HTTP exception.")
except CustomHTTPException as e:
    print(f"Exception caught: {e.description}")
