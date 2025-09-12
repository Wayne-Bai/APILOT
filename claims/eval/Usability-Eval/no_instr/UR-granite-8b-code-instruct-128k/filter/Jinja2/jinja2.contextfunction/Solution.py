from jinja2 import Environment, contextfunction
env = Environment()
@contextfunction
def my_context_function(context):
    return context
env.globals.update(my_context_function=my_context_function)
template = env.from_string("{{ my_context_function(context) }}")
