from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define a decorator function
def pass_context(func):
    def wrapper(*args, **kwargs):
        # Get the context from the kwargs
        context = kwargs.get('context', {})
        # Call the original function with the context as the first argument
        return func(*([context],) + args, **kwargs)
    return wrapper

# Define a template function
@pass_context
def template_func(context, *args, **kwargs):
    # Access the context variables in the template
    template = env.get_template('template.html')
    return template.render(context)

# Render the template with the context
context = {'name': 'John', 'age': 30}
print(template_func(context))
