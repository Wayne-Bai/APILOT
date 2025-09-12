from werkzeug.exceptions import HTTPException

class UserDefinedException(Exception):
    """ Custom user-defined base exception """
    pass

class CustomHTTPException(HTTPException, UserDefinedException):
    """ Exception that is a subclass of HTTPException and UserDefinedException """
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.code = 400  # Example: Bad Request
        self.description = description

# Example usage
if __name__ == "__main__":
    try:
        raise CustomHTTPException(description="This is a custom HTTP error.")
    except CustomHTTPException as e:
        print(f"Caught an exception: {e.description}, Status Code: {e.code}")
