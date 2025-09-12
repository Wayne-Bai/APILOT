from jinja2 import Environment, FileSystemLoader, template_rendered

def pass_environment(func):
    def wrapper(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return wrapper

@pass_environment
def render_template(env, template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

# Usage example
if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader('templates'))
    context = {'name': 'John Doe'}
    output = render_template(env, 'example_template.html', context)
    print(output)
