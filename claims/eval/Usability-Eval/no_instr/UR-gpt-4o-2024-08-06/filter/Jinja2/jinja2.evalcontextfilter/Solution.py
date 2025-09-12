from jinja2 import Environment, Template

# Create a custom filter that receives EvalContext
def custom_filter(value):
    def wrapper(eval_ctx, *args, **kwargs):
        # Access properties from eval_ctx if needed
        return value.upper()  # Example transformation
    return wrapper

env = Environment()

# Register the filter. Note: Normally, eval_ctx filters require @evalcontextfilter decorator,
# but here we mimic by assuming `custom_filter` is needed.
env.filters['custom'] = custom_filter

template = env.from_string("{{ text|custom }}")
rendered = template.render(text="hello world")

print(rendered)
