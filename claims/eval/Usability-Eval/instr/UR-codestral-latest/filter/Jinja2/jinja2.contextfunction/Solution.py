import jinja2

# Define the decorator
def context_decorator(func):
    def wrapper(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper

# Create a Jinja2 environment
env = jinja2.Environment()

# Define a template with a function
template = env.from_string("""
{% set result = my_function(context) %}
{{ result }}
""")

@context_decorator
def my_function(context):
    # Here, you can use the context to perform some operations
    return f"Hello, {context['name']}!"

# Add the function to the Jinja2 template's global namespace
env.globals['my_function'] = my_function

# Render the template with a context
print(template.render(context={'name': 'World'}))
