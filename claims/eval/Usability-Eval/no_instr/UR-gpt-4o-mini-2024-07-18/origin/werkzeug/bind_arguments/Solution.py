from werkzeug.utils import cached_property

def bind_args_to_dict(func):
    def wrapper(*args, **kwargs):
        bound_args = {
            'args': args,
            'kwargs': kwargs
        }
        return func(bound_args)
    return wrapper

@bind_args_to_dict
def my_function(arguments):
    return arguments

# Example usage
result = my_function(1, 2, key='value')
print(result)  # Output: {'args': (1, 2), 'kwargs': {'key': 'value'}}
