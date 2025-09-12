from jinja2 import pass_eval_context

@pass_eval_context
def a(eval_ctx, b):
    return b(eval_ctx.variables)
