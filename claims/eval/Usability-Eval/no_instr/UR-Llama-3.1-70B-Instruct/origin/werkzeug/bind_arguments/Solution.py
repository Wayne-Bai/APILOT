from werkzeug import LocalProxy, LocalStack
from werkzeug.local import release_local
from types import MethodType

def bind_arguments(func):
    def wrapper(*args, **kwargs):
        # Create a local stack
        local_stack = LocalStack()
        local_proxy = LocalProxy(lambda: local_stack.pop())

        # Bind arguments
        def set_arguments(self, *args, **kwargs):
            local_stack.push({'args': args, 'kwargs': kwargs})

        # Extend function with a method to bind arguments
        def bound_function(*args, **kwargs):
            bind_args_method = MethodType(set_arguments, func)
            bind_args_method(local_proxy, *args, **kwargs)
            return func(local_proxy)

        return bound_function(*args, **kwargs)

    return wrapper

# Example usage:
@bind_arguments
def add_numbers(proxy):
    arguments = proxy['args']
    return arguments[0] + arguments[1]

print(add_numbers(5, 7))  # Output: 12
