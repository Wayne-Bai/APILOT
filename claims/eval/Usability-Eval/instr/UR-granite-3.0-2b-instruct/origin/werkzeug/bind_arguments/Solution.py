from functools import wraps

def bind_args_to_dict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return args, kwargs
    return wrapper

@bind_args_to_dict
def my_function(arg1, arg2):
    return {"arg1": arg1, "arg2": arg2}

# Usage
result = my_function("Hello", 123)
print(result)  # Output: ('Hello', 123)
