
from jinja2 import Environment, FunctionLoader

def pass_environment(f):
    def wrapper(env, *args, **kwargs):
        return f(env, *args, **kwargs)
    return wrapper

env = Environment(loader=FunctionLoader(load_template))
@pass_environment
def render_template(env, template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

template_name = 'example_template.html'
context = {'name': 'John Doe', 'age': 30}
output = render_template(env, template_name, context)
print(output)
