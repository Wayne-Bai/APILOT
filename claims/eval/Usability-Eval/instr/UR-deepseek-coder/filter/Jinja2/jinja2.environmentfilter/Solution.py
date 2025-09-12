from jinja2 import Environment, FileSystemLoader

def render_template_with_env(env):
    def decorator(func):
        def wrapper(*args, **kwargs):
            template = env.get_template(kwargs.pop('template_name'))
            rendered_template = template.render(**kwargs)
            return func(env, rendered_template, *args, **kwargs)
        return wrapper
    return decorator

# Example usage:
if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader('templates'))

    @render_template_with_env(env)
    def my_function(env, rendered_template):
        print(rendered_template)

    my_function(template_name='example.html', name='World')
