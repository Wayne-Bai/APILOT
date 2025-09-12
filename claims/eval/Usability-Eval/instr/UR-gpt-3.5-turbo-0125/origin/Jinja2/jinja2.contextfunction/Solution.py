
from jinja2 import Environment, FileSystemLoader

def pass_context(f):
    def wrapper(*args, **kwargs):
        context = args[0]
        return f(context, *args[1:], **kwargs)

    return wrapper

env = Environment(loader=FileSystemLoader('templates'))
env.globals.update({
    'pass_context': pass_context
})

def render_template(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)
