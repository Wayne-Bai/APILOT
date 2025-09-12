
import Jinja2

def decorator(function):
    def wrapper(context, *args, **kwargs):
        return function(context, *args, **kwargs)
    return wrapper
