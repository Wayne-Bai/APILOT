from jinja2 import Template, Environment

# Define a class to create a pass Environment decorator
class PassEnvironment:
    def __init__(self, env):
        self.env = env

    # Use the __call__ method to call the decorated function with the Environment as the first argument
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Call the function with the arguments and Environment as the first argument
            return func(self.env, *args, **kwargs)
        return wrapper

# Create a Jinja2 Environment and a PassEnvironment instance
env = Environment(autoescape=True)
pass_env = PassEnvironment(env)

# Define a decorated function to render a template
@pass_env
def render_template(template, context):
    return env.get_template(template).render(context)

# Define a template
template = '''
Hello, {{ name }}!
'''

# Define a context
context = {'name': 'John'}

# Render the template using the PassEnvironment decorator
result = render_template('template', context)

# Print the result
print(result)
