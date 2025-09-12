from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    """A subclass of the calling HTTP exception."""

    def __init__(self, description=None, response=None):
        HTTPException.__init__(self, description, response)
        self.description = description
        self.response = response

    def __str__(self):
        return f"{self.__class__.__name__}: {str(self.description)}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {str(self.description)}>"

# Example Usage
try:
    # Some code that might raise your custom exception
    # ...
    raise CustomHTTPException(description="This is a custom exception",
                              response=make_response("Custom Exception Response"))
except CustomHTTPException as e:
    print(e)  # This will print "CustomHTTPException: This is a custom exception"
