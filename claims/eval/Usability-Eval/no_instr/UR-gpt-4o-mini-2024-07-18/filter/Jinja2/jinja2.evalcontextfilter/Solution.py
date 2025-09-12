from jinja2 import Environment, Template

def pass_eval_context(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

@pass_eval_context
def my_function(eval_context, name):
    return f"Hello, {name}! The current context is: {eval_context}"

# Example usage
env = Environment()
template = env.from_string("{{ my_function(eval_context, 'Alice') }}")

output = template.render(my_function=my_function, eval_context='Sample Context')
print(output)
