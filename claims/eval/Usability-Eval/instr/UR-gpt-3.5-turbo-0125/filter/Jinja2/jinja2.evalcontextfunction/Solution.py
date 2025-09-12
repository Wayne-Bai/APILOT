
from jinja2.environment import evalcontextfilter

def my_filter(eval_ctx, value):
    if eval_ctx is not None:
        value = value.upper()
    return value

env = Environment(autoescape=True)
env.filters['my_filter'] = evalcontextfilter(my_filter)
