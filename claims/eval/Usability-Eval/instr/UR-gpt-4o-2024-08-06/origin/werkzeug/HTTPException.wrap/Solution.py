from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.description = description
        self.response = response

    def get_description(self, environ=None):
        return self.description or "Custom HTTP Exception occurred."

    def __str__(self):
        return f"CustomHTTPException: {self.description}"
