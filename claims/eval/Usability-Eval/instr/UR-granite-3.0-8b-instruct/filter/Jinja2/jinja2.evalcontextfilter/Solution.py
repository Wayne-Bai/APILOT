from jinja2 import Environment, FileSystemLoader

def pass_eval_context(func):
    def wrapper(*args, **kwargs):
        eval_context = args[0]
        return func(eval_context, *args[1:], **kwargs)
    return wrapper

env = Environment(loader=FileSystemLoader('templates'))

@env.get_template('template.html').stream
@pass_eval_context
def render_template(eval_context, **kwargs):
    return env.get_template('template.html').render(eval_context)
