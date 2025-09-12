from functools import wraps

def bind_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bind_arguments
def my_function(arg1, arg2):
    return {"arg1": arg1, "arg2": arg2}

# Usage
result = my_function("Hello", 123)
print(result)
