from jinja2 import Environment, Template
from jinja2.ext import pass_eval_context

# Custom filter using pass_eval_context
@pass_eval_context
def custom_filter(eval_ctx, value):
    # Example modification using eval_ctx, not directly modifying anything here
    modified_value = value.upper()
    return modified_value

# Setup Jinja2 environment and register the custom filter
env = Environment()
env.filters['custom'] = custom_filter

# Sample template using the custom filter
template_source = '''
{{ "hello" | custom }}
'''

template = env.from_string(template_source)
result = template.render()

print(result)
