from jinja2 import Environment, FileSystemLoader

def pass_context(func):
    def wrapper(*args, **kwargs):
        context = args[0]
        return func(context, *args[1:], **kwargs)
    return wrapper

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

@pass_context
def render_template(context, *args, **kwargs):
    return template.render(context, *args, **kwargs)

# Usage
context = {'name': 'John', 'age': 30}
result = render_template(context, user='Jane')
