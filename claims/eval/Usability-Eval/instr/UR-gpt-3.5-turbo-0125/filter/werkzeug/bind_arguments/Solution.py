
# Importing the required modules from werkzeug
from werkzeug.datastructures import MultiDict

# Function to bind arguments into a dictionary
def bind_arguments(func, *args, **kwargs):
    provider = MultiDict(*args, **kwargs)
    return func(provider)

# Example function to be used with bind_arguments
def example_function(args):
    return args

# Example usage of bind_arguments function
result = bind_arguments(example_function, foo=1, bar='abc')
print(result)
