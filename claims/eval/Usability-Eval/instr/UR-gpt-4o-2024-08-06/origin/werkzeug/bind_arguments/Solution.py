from werkzeug.routing import Map, Rule
from werkzeug.routing import parse_rule

def bind_arguments(func, *args, **kwargs):
    # Parse the function signature
    func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
    # Create a dictionary to hold the bound arguments
    bound_arguments = {key: value for key, value in zip(func_args, args)}
    # Update with any keyword arguments given
    bound_arguments.update(kwargs)
    return bound_arguments

# Example usage
def my_function(arg1, arg2, arg3=3):
    pass

args = (1, 2)
kwargs = {'arg3': 4}
bound = bind_arguments(my_function, *args, **kwargs)
print(bound)
