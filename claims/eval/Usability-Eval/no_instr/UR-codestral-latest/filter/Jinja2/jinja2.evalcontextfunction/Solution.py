from jinja2 import Environment, Template, contextfunction

# Define the environment.
env = Environment()

# Define a decorator that takes and uses the EvalContext.
def use_eval_context(func):
    @contextfunction
    def wrapper_func(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper_func

# Use the decorator on a function that you want to use in your templates.
@use_eval_context
def my_function(ctx, arg1, arg2):
    # ctx is the EvalContext.
    # You can use it to access variables in the template scope.
    return arg1 + arg2

# Register the function with the environment.
env.globals['my_function'] = my_function

# Define a template that uses the function.
template = Template("{{ my_function(value1, value2) }}")

# Render the template with a context.
output = template.render(value1=1, value2=2)

print(output)
