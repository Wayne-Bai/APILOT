from werkzeug.exceptions import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, description=None, response=None):
        super(CustomHTTPException, self).__init__(description, response)

# Example procedure to raise the exception
def something_went_wrong():
    raise CustomHTTPException(description='An error occurred')

if __name__ == '__main__':
    try:
        something_went_wrong()
    except CustomHTTPException as e:
        print(e.description)
