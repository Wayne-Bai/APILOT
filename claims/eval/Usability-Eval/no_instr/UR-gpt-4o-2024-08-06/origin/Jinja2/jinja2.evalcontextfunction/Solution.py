from jinja2 import Environment, Template, evalcontextfilter

# Define a custom filter that requires the EvalContext
@evalcontextfilter
def reverse_string(eval_ctx, value):
    if eval_ctx.autoescape:
        # Perform some operation if autoescape is enabled
        value = value[::-1]
    return value

# Create an instance of the Jinja2 environment
env = Environment()

# Register the custom filter with the environment
env.filters['reverse_string'] = reverse_string

# Prepare a Jinja2 template string
template = Template("Reversed string: {{ 'Hello, World!' | reverse_string }}")

# Render the template without any specific context
rendered = template.render()

print(rendered)
