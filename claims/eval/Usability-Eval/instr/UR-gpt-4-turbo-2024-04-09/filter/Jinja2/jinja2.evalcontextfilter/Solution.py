from jinja2 import Environment, Template, pass_eval_context

@pass_eval_context
def custom_filter(eval_ctx, value):
    # Use eval_ctx to access the environment and data during template rendering
    if eval_ctx.autoescape:
        value = f"<escaped>{value}</escaped>"
    return value

# Creating an environment
env = Environment(autoescape=True)
env.filters['custom'] = custom_filter

# Example template using the custom filter
template = env.from_string("{{ 'Hello'|custom }}")

# Render the template
print(template.render())
