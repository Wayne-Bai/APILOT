from jinja2 import Environment, Template

def my_decorator(func):
    def wrapper(env, *args, **kwargs):
        # Call the decorated function with the environment as the first argument
        return func(env, *args, **kwargs)
    return wrapper

@my_decorator
def render_template(env, template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

# Example usage
env = Environment(loader=FileSystemLoader('templates'))
context = {'name': 'John'}
output = render_template(env, 'example_template.html', context)
print(output)
