from jinja2 import Environment, BaseLoader

def pass_eval_context(func):
    def wrapper(*args, **kwargs):
        eval_context = args[0]
        return func(eval_context, *args[1:], **kwargs)
    return wrapper

env = Environment(loader=BaseLoader())
env.globals['pass_eval_context'] = pass_eval_context

@env.globals['pass_eval_context']
def my_function(eval_context, arg1, arg2):
    # Your function code here
    pass
