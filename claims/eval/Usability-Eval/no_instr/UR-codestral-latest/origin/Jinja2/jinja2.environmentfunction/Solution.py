from jinja2 import Environment, PackageLoader, select_autoescape

# Define a decorator to accept Jinja2 Environment as the first argument
def use_jinja2(env):
    def decorator(fn):
        def wrapped(*args, **kwargs):
            # Call the function with the environment as the argument
            return fn(env, *args, **kwargs)
        return wrapped
    return decorator

# Define an environment
env = Environment(
    loader=PackageLoader("myapplication"),
    autoescape=select_autoescape()
)

# Use the decorator
@use_jinja2(env)
def render_template(env, template_name, **context):
    template = env.get_template(template_name)
    return template.render(context)

# Call the decorated function
rendered_output = render_template("my_template.html", welcome="Welcome to my site")
