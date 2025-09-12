from jinja2 import Environment, Template

def pass_eval_context(f):
    def wrapper(eval_context, *args, **kwargs):
        return f(eval_context, *args, **kwargs)
    wrapper.pass_eval_context = True
    return wrapper

@pass_eval_context
def custom_function(eval_context, value):
    return f"Modified: {value} with autoescaping={eval_context.autoescape}"

env = Environment(autoescape=True)
env.globals['custom_function'] = custom_function

template = env.from_string("{{ custom_function('Hello World') }}")
result = template.render()

print(result)
