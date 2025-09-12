from jinja2 import Environment, FileSystemLoader

def pass_env_to_decorated_function(func):
    def wrapper(*args, **kwargs):
        env = args[0]
        return func(env, *args[1:], **kwargs)
    return wrapper

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a template
template = env.get_template('my_template.html')

# Define a function to be decorated
@pass_env_to_decorated_function
def my_function(env):
    # Your function code here
    pass

# Render the template with the environment as the first argument
rendered_template = template.render(env=env)
