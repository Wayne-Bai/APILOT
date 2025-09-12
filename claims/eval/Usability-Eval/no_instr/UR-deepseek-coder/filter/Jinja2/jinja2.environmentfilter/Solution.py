from jinja2 import Environment, FileSystemLoader

def render_template_with_env(template_name, **context):
    def decorator(func):
        def wrapper(*args, **kwargs):
            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template(template_name)
            rendered_template = template.render(**context)
            return func(env, rendered_template, *args, **kwargs)
        return wrapper
    return decorator

# Example usage:
@render_template_with_env('example.html', name='John Doe')
def example_function(env, rendered_template, *args, **kwargs):
    print(rendered_template)
    # You can now use the 'env' object for further Jinja2 operations if needed

example_function()
