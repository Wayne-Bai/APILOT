import jinja2
from functools import wraps

# Create a Jinja2 Environment
jinja_env = jinja2.Environment()

def pass_context(func):
    """
    A decorator that passes the context as the first argument to the decorated function.
    
    Args:
        func: The function to be decorated.
    
    Returns:
        A wrapper function that passes the context to the decorated function.
    """
    
    @wraps(func)
    def wrapper(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    
    return wrapper

# Example usage:

@pass_context
def my_function(context, x, y):
    """
    An example function that uses the context and two other arguments.
    
    Args:
        context (dict): The context dictionary.
        x (int): The first number.
        y (int): The second number.
    
    Returns:
        The result of the operation.
    """
    return x + y

# Create a context dictionary
context = {"name": "John", "age": 30}

# Call the decorated function with the context and other arguments
result = my_function(context, 3, 5)
print(result)  # Output: 8
