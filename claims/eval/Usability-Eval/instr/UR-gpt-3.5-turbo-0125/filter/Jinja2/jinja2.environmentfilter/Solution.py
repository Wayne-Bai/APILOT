
from jinja2 import Environment, FunctionLoader

def my_function(environment, *args, **kwargs):
    # Access the environment variable and do something with it
    ...

# Create a custom function loader
loader = FunctionLoader(my_function)

# Create a Jinja2 environment with the custom function loader
env = Environment(loader=loader)

# Render a template with the custom function
template = env.from_string("{{ my_custom_function() }}")
output = template.render()

print(output)
