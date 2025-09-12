from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a decorator function
def pass_env(func):
    def wrapper(*args, **kwargs):
        # Pass the environment as the first argument
        return func(env, *args, **kwargs)
    return wrapper

# Use the decorator
@pass_env
def render_template(env, template_name, **context):
    # Render the template
    template = env.get_template(template_name)
    return template.render(context)

# Usage
template_name = 'example.html'
context = {'name': 'John'}
print(render_template(template_name, **context))
