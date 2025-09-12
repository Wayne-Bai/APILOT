
from jinja2 import Environment, FileSystemLoader

# Define the context dictionary
context = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Create an environment and a file system loader
env = Environment(loader=FileSystemLoader('.'))

# Define the decorator function
def render_template(template):
    return env.get_template(template).render(context)

# Decorate the function with the context dictionary
@render_template('greeting.html')
def greet():
    return 'Hello, {}!'.format(name)

# Render the template using the decorator
print(greet()) # Output: Hello, John Doe!
