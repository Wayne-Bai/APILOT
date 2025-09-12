from werkzeug.exceptions import BadRequest

class CustomBadRequest(BadRequest):
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)

# Example usage:
if not valid_input:
    raise CustomBadRequest("Your input was not valid.")
