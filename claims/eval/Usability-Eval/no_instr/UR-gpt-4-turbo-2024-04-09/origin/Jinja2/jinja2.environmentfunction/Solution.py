from jinja2 import Environment, Template

def pass_environment(func):
    """ Decorator to pass the Environment as the first argument to the function """
    def wrapper(environment, *args, **kwargs):
        return func(environment, *args, **kwargs)
    return wrapper

@pass_environment
def custom_function(env, x):
    """ Example function that uses the Environment and other arguments """
    # You can access the Environment attributes such as env.globals, env.filters, etc.
    return f"Function received environment with globals: {list(env.globals.keys())} and argument: {x}"

# Create a Jinja2 Environment and register the decorated function
env = Environment()
env.globals['custom_function'] = custom_function

# Create a template that calls the custom_function
template = env.from_string("{{ custom_function(99) }}")

# Render the template
rendered = template.render()
print(rendered)
