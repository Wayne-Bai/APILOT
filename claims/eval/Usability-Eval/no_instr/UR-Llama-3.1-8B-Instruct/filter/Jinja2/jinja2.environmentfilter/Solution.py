# Import required module
from jinja2 import Template, Environment
from functools import wraps

# Define a function that renders a template
def render_template(template_path, **kwargs):
    with open(template_path, 'r') as file:
        template = file.read()
    template = Template(template)
    return template.render(**kwargs)

# Define a decorator to pass the Environment to the decorated function
def pass_env(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        env = Environment()
        result = func(env, *args, **kwargs)
        return result
    return wrapper

# Define a template
template = """
 ctx = {{ env }}
"""

# Render the template with a new Environment
env = Environment()
rendered_template = render_template('template.txt', env=env)
print(rendered_template)

# Use the decorator to pass the Environment to a function
@pass_env
def example(env):
    ctx = env
    return ctx

example_context = example(Environment())
print(example_context)
