
from jinja2 import Template, Environment

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        context = EvalContext()
        return fn(context, *args, **kwargs)
    return wrapper

@my_decorator
def my_function(context, a, b):
    # do something with the EvalContext and a and b
    pass

template = Template("{{ my_function(a=1, b=2) }}")
rendered = template.render()
print(rendered)
