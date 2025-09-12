from jinja2 import Environment
import jinja2

def custom_filter(eval_ctx, value):
    # Your custom filter logic here
    return value

env = Environment()
env.filters['custom_filter'] = jinja2.pass_eval_context(custom_filter)
