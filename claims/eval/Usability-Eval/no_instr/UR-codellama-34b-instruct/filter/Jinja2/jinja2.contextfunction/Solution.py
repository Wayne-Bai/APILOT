
from jinja2 import Environment

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Get the template context from the arguments
        context = kwargs.get('context', {})
        # Call the original function with the context as the first argument
        return func(context, *args, **kwargs)
    return wrapper

# Create a Jinja2 environment and add the decorator to it
env = Environment()
env.add_decorator(my_decorator)

# Render a template using the environment
template = env.from_string("Hello {{ name }}!")
output = template.render({'name': 'John Doe'}, context=None)
print(output)  # Output: Hello John Doe!
