from jinja2 import Environment, contextfunction

# Define a template function that requires environment as the first argument
@contextfunction
def greeting_function(ctx, name):
    # Access environment from context if needed
    env = ctx.environment
    # Return a greeting message
    return f"Hello, {name}!"

# Create an environment and register the function
env = Environment()
env.globals['greet'] = greeting_function

# Create a simple template that uses the registered global function
template = env.from_string("{{ greet('World') }}")

# Render the template
rendered_output = template.render()
print(rendered_output)
