
from jinja2 import Environment

def decorator_function( decorated_function ):
    def wrapper( *args, **kwargs ):
        environment = Environment()
        return decorated_function( environment, *args, **kwargs )
    return wrapper
