
from jinja2 import Environment

def pass_env(func):
    def wrapper(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return wrapper

env = Environment()

@pass_env
def my_function(env):
    # Access the environment object here
    print(env)

# Call the decorated function with the environment object
my_function(env)
