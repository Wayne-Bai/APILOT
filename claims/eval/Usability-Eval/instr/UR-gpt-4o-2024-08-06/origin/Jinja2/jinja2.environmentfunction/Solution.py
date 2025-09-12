from jinja2 import Environment, Template, contextfunction

# Define a custom filter with Environment as the first argument
@contextfunction
def greet_user(context, name):
    env = context.environment
    return f"Hello, {name}! Welcome to the {env.globals.get('site_name', 'Default Site')}"

# Create an instance of the Environment
env = Environment()
env.globals['site_name'] = 'My Awesome Site'
env.filters['greet_user'] = greet_user

# Create a template that uses the custom filter
template_code = """
{{ 'Alice'|greet_user }}
"""

template = env.from_string(template_code)
rendered = template.render()
print(rendered)
