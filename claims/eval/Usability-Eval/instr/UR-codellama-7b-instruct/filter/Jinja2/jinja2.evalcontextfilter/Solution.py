
from jinja2 import Environment, EvalContext, Decorator

# Create a new Jinja2 environment
env = Environment()

# Define the decorator
@Decorator(eval_context=EvalContext)
def my_decorator(func):
    return func

# Use the decorator on a function
@my_decorator
def greet(name):
    print("Hello, {}!".format(name))

# Render a template using the EvalContext
eval_context = env.evaluate("{{ name }}", EvalContext(name='Alice'))
greet(eval_context)
