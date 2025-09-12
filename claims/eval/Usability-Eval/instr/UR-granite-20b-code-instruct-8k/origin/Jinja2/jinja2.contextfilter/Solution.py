from jinja2 import contextfunction

@contextfunction
def my_decorator(context, *args, **kwargs):
    return "Hello, World!"
