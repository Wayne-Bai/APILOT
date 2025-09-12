from jinja2 import Environment

def my_decorator(func):
    def wrapper(*args, **kwargs):
        env = kwargs.get("env")
        if not env:
            raise ValueError("Environment must be passed as a keyword argument.")
        return func(*args, **kwargs)
    return wrapper
