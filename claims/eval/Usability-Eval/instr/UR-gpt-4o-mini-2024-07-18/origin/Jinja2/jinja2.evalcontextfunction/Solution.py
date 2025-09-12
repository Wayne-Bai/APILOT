from jinja2 import Template, Environment

def my_decorator(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

@my_decorator
def my_function(eval_context, name):
    return f"Hello, {name}! Eval context: {eval_context}"

env = Environment()
template = env.from_string("{{ my_function('John') }}")
env.globals['my_function'] = my_function

# Render the template
output = template.render(my_function=my_function)
print(output)
