from jinja2 import Environment, evalcontextfilter

env = Environment()

@evalcontextfilter
def my_filter(eval_ctx, value):
    # do something with the EvalContext
    return value

template = env.from_string("{{ my_filter(value) }}")
output = template.render(value="Hello, world!")

print(output)  # prints "Hello, world!"
