
import jinja2

def pass_env(func):
    def wrapper(*args, **kwargs):
        env = kwargs.pop('env', None)
        if env is not None:
            func.__globals__['ENV'] = env
        return func(*args, **kwargs)
    return wrapper

@pass_env
def my_function(arg1, arg2):
    # do something with ENV here
    return arg1 + arg2
