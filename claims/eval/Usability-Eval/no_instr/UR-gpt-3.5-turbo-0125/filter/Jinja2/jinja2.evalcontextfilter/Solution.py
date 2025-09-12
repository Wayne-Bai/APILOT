
from jinja2 import Environment, FunctionLoader, evalcontextfilter, Markup, Undefined

env = Environment()


def my_filter(eval_ctx, value):
    # Your custom logic here
    pass


env.filters['my_filter'] = evalcontextfilter(my_filter)

template = env.from_string("{{ 'value' | my_filter }}")
output = template.render()
print(output)
