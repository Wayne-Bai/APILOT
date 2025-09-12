from jinja2 import Environment, contextfilter

env = Environment()

def requires_context(func):
    def wrapper(*args, **kwargs):
        ctx = args[0]
        return func(ctx, *args[1:], **kwargs)
    return wrapper

@env.filter
@requires_context
def custom_filter(ctx, value):
    # Now you can use 'ctx' which is an instance of jinja2.runtime.Context
    return value.upper()

template = env.from_string('{{ "hello world" | custom_filter }}')
print(template.render())
