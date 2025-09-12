
from jinja2 import Environment

# Define a decorator that passes the environment as the first argument
def pass_env(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Create an environment and register the decorator with it
env = Environment()
env.decorators = [pass_env]

# Define a function that uses the passed-in environment
@pass_env
def my_func(env):
    print("Environment:", env)

# Render a template that calls the decorated function
template = env.from_string("{% my_func() %}")
result = template.render()
print(result)
