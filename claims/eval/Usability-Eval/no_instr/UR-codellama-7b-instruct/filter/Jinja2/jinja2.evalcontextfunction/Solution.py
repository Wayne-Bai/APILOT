
from jinja2 import EvalContext

def custom_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before the decorated function is called
        func(*args, **kwargs)
        # Do something after the decorated function is called
    return wrapper
