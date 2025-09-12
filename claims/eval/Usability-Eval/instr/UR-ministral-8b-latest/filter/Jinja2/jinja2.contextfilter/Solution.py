from jinja2 import Environment, Template

# Decorator to pass the context to the decorated function
def pass_context(func):
    def wrapper(environment, **kwargs):
        # Get the context from the environment
        context = environment.templates.get() or {}
        context.update(kwargs)
        # Pass the context to the decorated function
        return func(context)
    return wrapper

# Example usage
if __name__ == "__main__":
    # Setup the Jinja2 environment and a template
    env = Environment()

    # Define a template
    template_str = """
{% if user_is_authenticated %}
    <p>Welcome, {{ user.name }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
"""

    template = Template(template_str)
    env.templates = {'template': template}  # For demonstration purposes

    # Decorated function
    @pass_context
    def render_template(context):
        return template.render(context)

    # Render the template with the context
    context = {'user': {'name': 'Alice', 'is_authenticated': True}}
    result = render_template(env, **context)

    print(result)
