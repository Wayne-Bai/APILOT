class CustomException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"Custom Exception: {self.message}, Error Code: {self.error_code}"
