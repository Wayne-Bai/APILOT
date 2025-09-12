from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment()

# Create a loader to read templates from a directory
loader = FileSystemLoader('templates')

# Load a template from the directory
template = env.get_template('my_template.html')

# Define a function to be decorated
def my_function():
    # Pass the environment as the first argument to the decorated function
    return template.render(env=env)

# Call the function
result = my_function()
