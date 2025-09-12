from jinja2 import Environment, Template

def pass_context_decorator(f):
    def wrapped(context, *args, **kwargs):
        return f(context, *args, **kwargs)
    return wrapped

@pass_context_decorator
def my_custom_function(context, name):
    return f"Hello {name}, you're accessing with context data: {context}"

# Creating Jinja2 environment
env = Environment()

# Example template with custom function usage
template = env.from_string('{{ custom_function(name) }}')
result = template.render(name="Alice", custom_function=my_custom_function)

print(result)
