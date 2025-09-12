from werkzeug.wrappers import Request, Response

def bind_arguments(func, *args, **kwargs):
    # Retrieve function arguments
    func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
    
    # Bind positional and keyword arguments
    bound_arguments = {}
    bound_arguments.update(zip(func_args, args))
    bound_arguments.update(kwargs)
    
    return bound_arguments

# Example function to test argument binding
def example_function(arg1, arg2, arg3=None):
    pass

# Bind arguments for the example function
arguments = bind_arguments(example_function, 'value1', 'value2', arg3='value3')
print(arguments)
