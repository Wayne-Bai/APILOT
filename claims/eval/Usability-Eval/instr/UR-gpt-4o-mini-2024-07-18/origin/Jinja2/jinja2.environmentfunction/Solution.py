from jinja2 import Environment, Template

def pass_environment(func):
    def wrapper(env, *args, **kwargs):
        return func(env, *args, **kwargs)
    return wrapper

@pass_environment
def render_template(env, template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

# Example usage
if __name__ == "__main__":
    env = Environment(loader=... )  # Specify the loader as per your requirements
    context = {'variable': 'value'}
    rendered = render_template(env, 'example_template.html', context)
    print(rendered)
