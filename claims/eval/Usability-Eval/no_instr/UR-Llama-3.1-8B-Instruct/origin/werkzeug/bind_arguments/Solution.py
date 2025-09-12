from functools import wraps

# Define a function that takes in a function and binds its arguments into a dict
def bind_arguments(func):
    """
    Binds the arguments passed to a function into a dictionary.

    Args:
        func: The target function

    Returns:
        A wrapped function that binds the arguments into a dictionary
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Bind the arguments into a dictionary
        bound_args = kwargs
        
        # Check if *args are provided
        if args:
            # Add positional arguments to the bound_args dictionary
            # If any positional argument is not provided as a kwarg, use its index as key
            for idx, arg in enumerate(args):
                bound_args[f"arg_{idx}"] = arg
        
        # Call the target function with the bound arguments
        return func(**bound_args)
    
    return wrapper

# Example usage:

@bind_arguments
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

print(greet("John", 30))  # Output: Hello, John! You are 30 years old.
print(greet(age=25, name="Jane"))  # Output: Hello, Jane! You are 25 years old.
