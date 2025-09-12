from jinja2 import Environment

def jinja2_decorator(func):
    def wrapper(self, env, *args, **kwargs):
        return func(self, *args, **kwargs)
    return wrapper

# Here is how you can use the decorated function
@jinja2_decorator
def my_function(self, arg1, arg2):
    # your implementation here
    pass

# Call the decorated function with Environment(autoescape=True) object
env = Environment(autoescape=True)
result = my_function(env, 'argument1', 'argument2')
