from jinja2 import Environment, Template

def pass_eval_context(f):
    """Decorator to pass the evaluation context to a function."""
    def new_func(eval_ctx, *args, **kwargs):
        return f(eval_ctx, *args, **kwargs)
    return new_func

@pass_eval_context
def custom_filter(eval_ctx, value):
    return f"Modified context value: {value} with autoescape= {eval_ctx.autoescape}"

# Set up Jinja2 environment
env = Environment(autoescape=True)
env.filters['custom_filter'] = custom_filter

# Create a template and render it
template = env.from_string("{{ 'Hello, Jinja2!' | custom_filter }}")
rendered = template.render()
print(rendered)
