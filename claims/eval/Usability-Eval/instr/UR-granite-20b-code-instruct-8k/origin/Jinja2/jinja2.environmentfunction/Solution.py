from jinja2 import Environment, FileSystemLoader

def decorator_function(function):
    def wrapper(*args, **kwargs):
        env = Environment(loader=FileSystemLoader('templates'))
        return function(env, *args, **kwargs)
    return wrapper
