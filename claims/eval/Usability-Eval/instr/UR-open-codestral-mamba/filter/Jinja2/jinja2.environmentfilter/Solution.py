from jinja2 import Environment, BaseLoader

# Define the Environment
env = Environment(loader=BaseLoader, autoescape=True)

# Define the decorated function
def template_renderer(func):
    def wrapper(*args, **kwargs):
        # Render template
        return env.get_template(func.__name__).render(*args, **kwargs)
    return wrapper

# Example usage:
@template_renderer
def index_template(name):
    return "Hello, {{ name }}!"

print(index_template(name="Alice"))  # Outputs: 'Hello, Alice!'
