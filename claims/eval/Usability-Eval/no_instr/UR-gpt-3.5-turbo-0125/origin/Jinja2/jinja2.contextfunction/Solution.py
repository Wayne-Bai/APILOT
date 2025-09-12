
from jinja2 import Template


def pass_context_decorator(func):
    def wrapper(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper


@pass_context_decorator
def my_template(context):
    # Your template rendering logic here
    pass


# Example Usage
context = {'name': 'Alice', 'age': 30}
rendered_template = my_template(context)
