from jinja2 import Environment, FileSystemLoader, select_autoescape
 
env = Environment(
 loader=FileSystemLoader('templates'),
 autoescape=select_autoescape(['html', 'xml'])
)
 
def template_decorator(func):
    def wrapper(*args, **kwargs):
        environment = args[0]
        print(environment)
        return func(*args, **kwargs)
    return wrapper
 
@template_decorator
def render_template(environment, template_name, context):
    template = environment.get_template(template_name)
    return template.render(context)
