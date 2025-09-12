from werkzeug import exceptions
from werkzeug.wrappers import Request, Response

# Create a subclass of the HTTP exception
class CustomHttpException(exceptions.HTTPException):
    def __init__(self, description=None, exception=None):
        super().__init__(description)
        
        # Create an exception that is a subclass of the calling HTTP exception and the exception argument
        if exception:
            exception_class = type('HttpException_' + type(exception).__name__, (type(exception), self.__class__), {})
            raise exception_class(description)

# Example usage
def application(environ, start_response):
    request = Request(environ)
    try:
        # Simulate an error
        raise ValueError('Invalid value')
    except exceptions.HTTPException as e:
        # Create a custom HTTP exception
        http_exception = CustomHttpException(description='Invalid request', exception=e)
        return http_exception(environ, start_response)
    except Exception as e:
        # Create a custom HTTP exception
        http_exception = CustomHttpException(description='Internal server error', exception=e)
        return http_exception(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application, use_debugger=True, use_reloader=True)
