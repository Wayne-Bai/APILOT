
from werkzeug.datastructures import MultiDict
from inspect import signature

def bind_arguments(function, query_params):
    """
    Binds query parameters to function arguments.
    
    :param function: The function to which arguments need to be bound.
    :param query_params: Dictionary or MultiDict of query parameters.
    :return: Dictionary with function argument names bound to their respective values from query_params.
    """
    sig = signature(function)
    bound_args = {}
    
    for param in sig.parameters:
        if param in query_params:
            bound_args[param] = query_params[param]
        else:
            # Handle missing parameters
            if sig.parameters[param].default is not sig.parameters[param].empty:
                bound_args[param] = sig.parameters[param].default
            else:
                raise ValueError(f"Missing required parameter: {param}")
    
    return bound_args

# Example usage
def example_function(name, age, city="Unknown"):
    return f"Name: {name}, Age: {age}, City: {city}"

# Simulate query parameters
query_params = MultiDict([
    ('name', 'John'),
    ('age', '30')
])

bound_arguments = bind_arguments(example_function, query_params)
print(bound_arguments)
