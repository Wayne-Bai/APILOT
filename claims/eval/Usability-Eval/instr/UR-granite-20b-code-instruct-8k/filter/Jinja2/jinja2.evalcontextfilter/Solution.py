from jinja2 import Environment, FileSystemLoader

def pass_eval_context(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template('example.html')

@pass_eval_context
def render_template(eval_context, template_name, **context):
    template = env.get_template(template_name)
    return template.render(context)

eval_context = EvalContext()
result = render_template(eval_context, 'example.html', name='John')
