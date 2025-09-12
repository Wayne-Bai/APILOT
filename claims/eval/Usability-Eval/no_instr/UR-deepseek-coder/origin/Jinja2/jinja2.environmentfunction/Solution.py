from jinja2 import Environment, FileSystemLoader

def render_template_with_env(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    return template.render(**kwargs)

@render_template_with_env
def my_function(env, **kwargs):
    # Use the environment object here if needed
    return env.get_template('my_template.html').render(**kwargs)

# Example usage
result = my_function(template_name='my_template.html', name='Alice')
print(result)
