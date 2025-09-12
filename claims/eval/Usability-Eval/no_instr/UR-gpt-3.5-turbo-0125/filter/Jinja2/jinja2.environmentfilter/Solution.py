
from jinja2 import Environment, FileSystemLoader

def pass_environment(func):
    def inner(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return inner

env = Environment(loader=FileSystemLoader('templates'))

@pass_environment
def my_function(env, template_name):
    template = env.get_template(template_name)
    return template.render()

# Example usage
print(my_function(env, 'my_template.html'))
