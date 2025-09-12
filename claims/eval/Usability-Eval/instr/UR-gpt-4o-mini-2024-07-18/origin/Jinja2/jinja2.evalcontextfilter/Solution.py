from jinja2 import Environment, FileSystemLoader

def pass_eval_context(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

@pass_eval_context
def my_function(eval_context, name):
    return f"Hello, {name}! Your context is: {eval_context}"

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Example template rendering
template = env.get_template('my_template.html')

# Render the template with context
eval_context = {'some_key': 'some_value'}
output = template.render(my_function=my_function, name="John", eval_context=eval_context)

print(output)
