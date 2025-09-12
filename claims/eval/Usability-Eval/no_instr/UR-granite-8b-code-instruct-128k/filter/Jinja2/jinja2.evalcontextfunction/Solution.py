from jinja2 import Environment, BaseLoader, evalcontextfilter

# Create a Jinja2 environment
env = Environment(loader=BaseLoader)

# Define a decorator that takes the EvalContext as the first argument
@evalcontextfilter
def my_filter(eval_ctx, value):
    # Do something with the EvalContext
    return value

# Register the decorator with the environment
env.filters['my_filter'] = my_filter

# Render a template using the decorator
template = env.from_string("{{ my_filter(value) }}")
context = {'value': 'Hello, World!'}
output = template.render(context)

print(output)  # Output: Hello, World!
