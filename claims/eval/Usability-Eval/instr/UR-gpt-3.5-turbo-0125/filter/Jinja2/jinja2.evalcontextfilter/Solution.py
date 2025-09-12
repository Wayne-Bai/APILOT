
from jinja2 import Template, Environment, meta

def my_decorator(func):
    def wrapper(eval_ctx, *args, **kwargs):
        return func(eval_ctx, *args, **kwargs)
    return wrapper

env = Environment()
env.tests['my_decorator'] = my_decorator

template = env.from_string("{{ test_var|my_decorator }}")
parsed_template = env.parse(template)
eval_ctx = meta.find_undeclared_variables(parsed_template)

output = template.render(test_var='Hello World', _eval_ctx=eval_ctx)
print(output)
