from jinja2 import Template

# Define a function that needs to be decorated
def my_function(context):
    # Example logic that uses the context
    return f"Hello, {context['name']}!"

# Decorate the function to pass the context as the first argument
def pass_context(func):
    def wrapper(template_context, *args, **kwargs):
        return func(template_context, *args, **kwargs)
    return wrapper

# Apply the decorator
decorated_function = pass_context(my_function)

# Example context
context = {
    'name': 'Alice'
}

# Example template
template_source = "Result of the decorated function: {{ result }}"

# Create the Jinja2 template
template = Template(template_source)

# Render the template with the result from the decorated function
rendered_output = template.render(result=decorated_function(context))

print(rendered_output)
