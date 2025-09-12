
# Importing the required module from werkzeug
from werkzeug.datastructures import MultiDict

# Function to bind arguments into a dictionary
def bind_arguments(func, *args, **kwargs):
    bound_args = {}

    # Binding positional arguments
    argspec = inspect.getfullargspec(func)
    for i in range(min(len(args), len(argspec.args))):
        bound_args[argspec.args[i]] = args[i]

    # Binding keyword arguments
    for key, value in kwargs.items():
        if key in argspec.args:
            bound_args[key] = value

    # Creating a MultiDict object
    bound_dict = MultiDict(bound_args)

    return bound_dict

# Example function to test binding
def example_function(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

# Testing the bind_arguments function
bound_args = bind_arguments(example_function, 'Alice', city='New York', unknown_arg='test')
print(bound_args)

