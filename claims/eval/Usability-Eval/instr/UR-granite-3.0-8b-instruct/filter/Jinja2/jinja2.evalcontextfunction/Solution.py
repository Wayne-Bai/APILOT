from jinja2 import Environment, Context

def pass_eval_context(func):
    def wrapper(*args, **kwargs):
        eval_context = Context(autoescape=False)
        return func(eval_context, *args, **kwargs)
    return wrapper

# Example usage:
@pass_eval_context
def my_function(eval_context, arg1, arg2):
    # Access eval_context.globals here if needed
    pass

# In your template:
{{ my_function('arg1', 'arg2') }}
