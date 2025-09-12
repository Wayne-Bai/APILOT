from jinja2 import Environment, BaseLoader

def pass_context(func):
    def wrapper(*args, **kwargs):
        context = args[0]
        return func(context, *args[1:], **kwargs)
    return wrapper

env = Environment(loader=BaseLoader())

@env.get_template('template.html')
def template(context):
    return env.get_template('template.html').render(context=context)

@pass_context
def render_template(context):
    return template(context)
