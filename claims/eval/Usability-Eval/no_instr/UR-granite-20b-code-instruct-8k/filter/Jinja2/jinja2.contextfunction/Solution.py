from jinja2 import contextfunction

@contextfunction
def pass_context(context, arg1, arg2):
    return f'The context is {context}, argument 1 is {arg1}, and argument 2 is {arg2}'
