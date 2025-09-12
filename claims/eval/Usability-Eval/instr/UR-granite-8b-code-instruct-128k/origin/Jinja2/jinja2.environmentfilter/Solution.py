from jinja2 import Environment
def pass_environment(func):
    def wrapper(*args, **kwargs):
        environment = args[0]
        return func(*args, **kwargs)
    return wrapper
@pass_environment
def render_template(environment, template_name, context):
    template = environment.get_template(template_name)
    return template.render(context)
