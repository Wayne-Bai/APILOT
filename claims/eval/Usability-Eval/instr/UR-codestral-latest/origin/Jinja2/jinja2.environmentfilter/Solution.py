from jinja2 import Environment, FileSystemLoader

def my_decorator(func):
    def wrapper(*args, **kwargs):
        env = args[0]
        # Add any custom logic here that uses the Jinja2 Environment
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def render_template(env, template_name, **context):
    template = env.get_template(template_name)
    return template.render(context)

# Load templates from the /templates directory
env = Environment(loader = FileSystemLoader('templates'))

# Render the template with some context
output = render_template(env, 'my_template.html', name='John Doe', age=30)

print(output)
