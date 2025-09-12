
from werkzeug import utils

def bind_arguments(func, *args):
    """
    Binds the given arguments to the given function and returns a dictionary containing
    the argument names and values.
    """
    # Get the function signature
    sig = inspect.signature(func)
    
    # Create a dictionary to store the bound arguments
    bound_args = {}
    
    # Iterate over the function parameters
    for name, param in sig.parameters.items():
        # Check if the parameter is a positional argument
        if param.kind == inspect.Parameter.POSITIONAL_ONLY:
            # Get the argument value from the arguments tuple
            arg = args[param.position]
            
            # Add the argument to the dictionary
            bound_args[name] = arg
        
        # Check if the parameter is a keyword argument
        elif param.kind == inspect.Parameter.KEYWORD_ONLY:
            # Get the argument value from the arguments dict
            arg = args[name]
            
            # Add the argument to the dictionary
            bound_args[name] = arg
    
    return bound_args
