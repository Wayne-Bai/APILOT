from jinja2 import Environment, FileSystemLoader

def pass_context(func):
    def wrapper(*args, **kwargs):
        context = kwargs.pop('context', {})
        return func(*args, **context, **kwargs)
    return wrapper

def render_template(template_name, **context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_name)
    return template.render(**context)
