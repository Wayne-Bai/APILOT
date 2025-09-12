from jinja2 import Environment, FileSystemLoader

# Create an environment and load templates from a directory
env = Environment(loader=FileSystemLoader('templates'))

def pass_environment_as_first_argument(func):
    def wrapper(*args, **kwargs):
        env = kwargs.get('env')
        if env is None:
            raise ValueError('No "env" provided in kwargs.')
        return func(env, *args, **kwargs)
    return wrapper

# Sample usage:
@pass_environment_as_first_argument
def some_template_function(env, template_name, context, **kwargs):
    # Render the template passing context
    template = env.get_template(template_name)
    return template.render(context, **kwargs)

# Example call
template_name = 'example_template.html'
context = {'key': 'value'}
result = some_template_function(env, template_name, context)
print(result)
