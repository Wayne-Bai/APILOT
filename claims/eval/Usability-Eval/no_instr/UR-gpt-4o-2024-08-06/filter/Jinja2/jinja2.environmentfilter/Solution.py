import jinja2
from jinja2 import Environment, Template, contextfunction

# Define a function with the contextfunction decorator that requires the environment as an argument
@contextfunction
def greet_function(context, name):
    # access the environment from the context
    environment = context.environment
    return f"Hello, {name}! Using environment: {environment}"

# Create an environment and register the custom function
env = Environment()
env.globals['greet'] = greet_function

# Create a template that uses the custom function
template_source = """
{% set user_name = 'Alice' %}
{{ greet(user_name) }}
"""

# Load the template
template = env.from_string(template_source)

# Render the template and print the result
output = template.render()
print(output)
