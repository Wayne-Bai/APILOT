from jinja2 import pass_eval_context

@pass_eval_context
def my_decorator(eval_context, *args, **kwargs):
    # do something with the eval_context
    return some_function(*args, **kwargs)
