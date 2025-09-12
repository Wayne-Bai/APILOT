from jinja2 import Environment, FunctionLoader
# Define a function that takes the context as the first argument
def my_decorator(func):
    def wrapper(*args, **kwargs):
        context = args[0]
        # Do something with the context
        print(f'The context is: {context}')
        # Call the original function with the remaining arguments
        return func(*args[1:], **kwargs)
    return wrapper
# Define a function that will be decorated
@my_decorator
def my_function(context, arg1, arg2):
    print(f'The arguments are: {arg1}, {arg2}')
# Create a context dictionary
context = {'key1': 'value1', 'key2': 'value2'}
# Call the decorated function with the context and arguments
my_function(context, 'arg1', 'arg2')
