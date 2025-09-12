from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a decorator function
def pass_environment(func):
    def wrapper(*args, **kwargs):
        # Pass the environment to the decorated function
        return func(env, *args, **kwargs)
    return wrapper

# Define a template function
@pass_environment
def render_template(env, template_name, **context):
    # Render the template with the given context
    template = env.get_template(template_name)
    return template.render(context)
