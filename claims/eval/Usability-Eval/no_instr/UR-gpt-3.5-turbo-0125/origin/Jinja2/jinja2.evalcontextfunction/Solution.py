
from jinja2 import Environment, FunctionLoader, evalcontextfilter, Markup

def my_filter(eval_ctx, value):
    if eval_ctx.autoescape:
        value = Markup(value)
    return value.upper()

env = Environment()
env.filters['my_filter'] = evalcontextfilter(my_filter)

template = env.from_string("{{ 'hello' | my_filter }}")
output = template.render()
print(output)
