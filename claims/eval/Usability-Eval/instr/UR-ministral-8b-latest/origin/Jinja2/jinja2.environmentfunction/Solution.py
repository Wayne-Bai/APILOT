from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment and set the template loader
env = Environment(loader=FileSystemLoader('templates'))

# Define a decorator function
def pass_env(first_arg):
    def decorator(func):
        def wrapper(env, *args, **kwargs):
            return func(func, kwargs.get("template", None), env, *args)
        return wrapper
    return decorator

# Use the decorator in a function
@pass_env
def render_template(func, template_name, env):
    return env.get_template(template_name).render()

# Example usage
template = env.get_template('example_template.html')

render_template(func=template, env=env)
