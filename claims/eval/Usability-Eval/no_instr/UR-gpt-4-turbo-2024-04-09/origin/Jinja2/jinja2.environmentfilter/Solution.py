from jinja2 import Environment, Template

def pass_environment(func):
    """Decorator to pass the environment as the first argument to the function."""
    def wrapper(environment, *args, **kwargs):
        return func(environment, *args, **kwargs)
    return wrapper

@pass_environment
def get_message(env, user):
    return f"Hello, {user}! Rendering using environment {env}"

# Create a Jinja2 environment
env = Environment()

# Create a template
template_source = "{{ get_message(user) }}"
template = env.from_string(template_source)

# Register the function with access to the environment
env.globals['get_message'] = get_message

# Render template
rendered_template = template.render(user="Alice")
print(rendered_template)
