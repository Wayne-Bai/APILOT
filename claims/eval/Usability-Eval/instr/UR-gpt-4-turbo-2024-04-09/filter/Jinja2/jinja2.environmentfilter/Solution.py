from jinja2 import Environment, FunctionLoader

def pass_environment(func):
    def wrapper(environment, *args, **kwargs):
        return func(environment, *args, **kwargs)
    return wrapper

# Example usage of the decorator
@pass_environment
def add_hello(environment, name):
    return f"Hello, {name} from {environment}"

# Setup a simple template
template = "{{ add_hello('John') }}"

# Create a Jinja2 environment with the decorated function 
env = Environment(loader=FunctionLoader(lambda name: template))
env.globals['add_hello'] = add_hello

# Render the template
print(env.render())
