from jinja2 import Environment, Template

# Create a Jinja2 environment
env = Environment()

# Decorator to pass a context as the first argument to the decorated function
def pass_context(template_string):
    template = env.from_string(template_string)
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = template.render(**kwargs)
            return func(context, *args, **kwargs)
        return wrapper
    return decorator

# Example template and function to use with the decorator
template_string = "Hello, {{ name }}!"

@pass_context(template_string)
def greet(context, name):
    print(context)

# Calling the wrapped function
greet(name='World')
