from jinja2 import Environment, FileSystemLoader

def my_decorator(func):
    def wrapper(context):
        return func(context)
    return wrapper

@my_decorator
def render_template(context):
    # Assuming you have a template that uses variables from context
    template_name = context.get('template_name', 'default_template.html')
    return environment.get_template(template_name).render(context)

# Set up the Jinja2 environment
file_loader = FileSystemLoader('templates')  # Replace 'templates' with your template folder
environment = Environment(loader=file_loader)

# Example context
context = {
    'template_name': 'example.html',  # Template file you want to render
    'title': 'Hello, World!',
    'content': 'Welcome to Jinja2 templating.',
}

# Render the template with the context
output = render_template(context)
print(output)
