from jinja2 import Environment, FileSystemLoader

def render_template(template_name, environment, *args, **kwargs):
    environment.from_string(template_name)
    return environment.render(*args, **kwargs)

# Create a Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Define the function to be decorated
def decorated_function():
    # Pass the environment as the first argument to the function
    env['function_name'] = decorated_function
    return render_template('template.html', env, function_name='decorated_function')

# Call the decorated function
result = decorated_function()
print(result)
