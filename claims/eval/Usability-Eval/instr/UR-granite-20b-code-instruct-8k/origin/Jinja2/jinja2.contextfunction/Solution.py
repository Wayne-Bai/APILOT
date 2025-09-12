from jinja2 import contextfilter

@contextfilter
def pass_context(ctx, func):
    return func(ctx)
