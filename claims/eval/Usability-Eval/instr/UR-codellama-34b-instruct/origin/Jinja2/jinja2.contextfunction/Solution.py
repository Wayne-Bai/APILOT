
from jinja2 import Template

def add_context(function):
    def wrapper(*args, **kwargs):
        context = args[0]
        return function(context)
    return wrapper

@add_context
def my_template(context):
    print(context.data)

template = Template("Hello {{ name }}!")
context = {"name": "Alice"}
result = template.render(my_template, context)
print(result)
