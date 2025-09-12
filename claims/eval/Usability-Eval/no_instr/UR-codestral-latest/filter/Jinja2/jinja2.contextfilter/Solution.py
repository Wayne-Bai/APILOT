from jinja2 import Environment, Template

def decorate_function(func):
    def wrapper(**kwargs):
        return func(kwargs['context'])
    return wrapper

@decorate_function
def my_function(context):
    env = Environment()
    template = env.from_string('Hello, {{ name }}!')
    return template.render(**context)

# Use the function
context = {'name': 'World'}
print(my_function(context=context))
