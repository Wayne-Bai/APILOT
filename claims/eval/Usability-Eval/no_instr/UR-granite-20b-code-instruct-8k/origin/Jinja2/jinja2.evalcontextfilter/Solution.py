import jinja2

def pass_eval_context(func):
    """Decorator that passes the Jinja2 EvalContext as the first argument to the decorated function."""
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper
