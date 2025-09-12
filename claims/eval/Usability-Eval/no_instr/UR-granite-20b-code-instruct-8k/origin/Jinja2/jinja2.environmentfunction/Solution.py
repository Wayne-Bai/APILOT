from jinja2 import Environment

def decorator(function):
    def wrapper(env, *args, **kwargs):
        return function(env, *args, **kwargs)
    return wrapper
