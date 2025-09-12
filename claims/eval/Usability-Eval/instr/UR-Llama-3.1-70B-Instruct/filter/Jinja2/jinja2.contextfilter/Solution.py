from jinja2 import Template, Dict

# Define a decorator to pass the context as the first argument to the decorated function
def pass_context(func):
    def wrapper(template, context, *args, **kwargs):
        return func(context, template, *args, **kwargs)
    return wrapper

# Define a function with the decorator
@pass_context
def render_template(context, template, *args, **kwargs):
    return template.render(context)

# Create a Jinja template
template = Template("Hello, {{ name }}!")

# Create a context dictionary
context = Dict([("name", "John")])

# Render the template with the context
result = render_template(template, context)

print(result)  # Output: Hello, John!
