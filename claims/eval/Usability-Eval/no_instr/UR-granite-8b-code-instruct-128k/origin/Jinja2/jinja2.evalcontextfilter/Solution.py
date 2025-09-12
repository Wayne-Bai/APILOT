from jinja2 import Environment, evalcontext

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with evalcontextfilter(Environment().unwrap(args[0])) as ctx:
            return func(*args, **kwargs)
    return wrapper
