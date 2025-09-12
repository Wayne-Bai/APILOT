from jinja2 import Environment, FileSystemLoader

# Define a simple decorator to pass context as the first argument
def pass_context(func):
    def wrapper(*args, **kwargs):
        # Assuming the first argument will be the context
        context = args[0]
        return func(context, *args[1:], **kwargs)
    return wrapper

@pass_context
def render_template(context, template_name, **kwargs):
    # Load template from environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    return template.render(context)

# Example usage
context = {'title': 'Hello, Jinja2!', 'message': 'This is how you use decorators with Jinja2.'}
output = render_template(context, 'example_template.html')
print(output)
