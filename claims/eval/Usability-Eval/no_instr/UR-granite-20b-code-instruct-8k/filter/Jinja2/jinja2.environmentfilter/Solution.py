from jinja2 import Environment, FileSystemLoader

def my_decorator(func):
    def wrapper(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return wrapper

@my_decorator
def my_function(env, template_name, context=None):
    if context is None:
        context = {}
    template = env.get_template(template_name)
    return template.render(context)

# Create an environment with a loader
env = Environment(loader=FileSystemLoader('/path/to/templates/'))

# Render a template
output = my_function(env, 'my_template.html', {'name': 'John Doe'})
