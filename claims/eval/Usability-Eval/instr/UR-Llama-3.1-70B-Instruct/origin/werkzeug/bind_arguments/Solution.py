from werkzeug.local import LocalProxy
from werkzeug.wrappers import Request, Response
from inspect import signature, Parameter
from functools import wraps

# Create a sample request
environ = {
    'wsgi.url_scheme': 'http',
    'wsgi.input': '',
    'QUERY_STRING': 'name=John&age=30',
    'REQUEST_METHOD': 'GET',
    'SCRIPT_NAME': '', 'PATH_INFO': '/'
}
request = Request(environ)

# Create a proxy for request.args
args_proxy = LocalProxy(lambda: request.args)

# Function to bind arguments to a dict
def bind_args(func):
    """
    Bind the arguments provided into a dict when passed a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the function parameters
        params = signature(func).parameters
        
        # Create a dictionary of function arguments
        func_args = {}
        
        # Iterate over the parameters
        for param_name, param in params.items():
            if param.default is not Parameter.empty:
                continue
            
            # Try to get the value from the request arguments
            if param_name in args_proxy:
                func_args[param_name] = args_proxy[param_name]
            else:
                # If the argument is not found in the request arguments, try to get it from the function arguments
                if param_name in kwargs:
                    func_args[param_name] = kwargs[param_name]
                else:
                    raise ValueError(f"Missing required argument '{param_name}'")
        
        # Call the function with the bound arguments
        return func(**func_args)
    
    return wrapper

# Example usage:
@bind_args
def greet(name, age):
    return Response(f'Hello, {name}! You are {age} years old.')

# Call the decorated function
response = greet()
print(response.response)
