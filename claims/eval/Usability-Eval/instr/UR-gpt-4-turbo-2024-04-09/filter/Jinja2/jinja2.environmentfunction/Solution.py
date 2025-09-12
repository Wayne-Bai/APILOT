from jinja2 import Environment, FileSystemLoader

# Custom decorator to inject the environment
def with_environment(f):
    def wrapper(environment, *args, **kwargs):
        return f(environment, *args, **kwargs)
    return wrapper

# Example using the decorator to a function
@with_environment
def get_info(environment, var_name):
    return f"The variable {var_name} is in a template processed by environment {environment}."

# Setup the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Adding the function to the environment globals
env.globals['get_info'] = get_info

# Sample usage
template = env.get_template('sample_template.html')
rendered = template.render(var_name='example')

print(rendered)
