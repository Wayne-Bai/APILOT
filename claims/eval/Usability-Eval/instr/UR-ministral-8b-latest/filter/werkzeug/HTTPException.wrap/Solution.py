from werkzeug.exceptions import HTTPException

# Define a custom exception class that inherits from werkzeug.exceptions.HTTPException
class MyCustomException(HTTPException):
    code = 418
    description = "I'm a teapot"

# Raise the custom exception
def some_function():
    raise MyCustomException(description="Raising a custom exception message")

try:
    some_function()
except MyCustomException as e:
    print(f"Caught a {e.code} exception: {e.description}")
