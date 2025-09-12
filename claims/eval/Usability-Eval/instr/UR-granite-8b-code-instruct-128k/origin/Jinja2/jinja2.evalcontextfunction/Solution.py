
from jinja2 import Environment, evalcontextfilter
env = Environment()
@evalcontextfilter
def my_filter(eval_ctx, value):
    # Use eval_ctx to access the current context
    return value.upper()
env.filters['my_filter'] = my_filter
template = env.from_string("{{ 'hello' | my_filter }}")
output = template.render()
print(output)  # Output: 'HELLO'
