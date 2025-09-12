from jinja2 import Environment, Template

def my_decorator(func):
    def wrapper(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return wrapper

@my_decorator
def render_template(env, template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

# Example usage
if __name__ == "__main__":
    env = Environment(loader=jinja2.FileSystemLoader('templates'))
    context = {'name': 'John'}
    output = render_template(env, 'my_template.html', context)
    print(output)
