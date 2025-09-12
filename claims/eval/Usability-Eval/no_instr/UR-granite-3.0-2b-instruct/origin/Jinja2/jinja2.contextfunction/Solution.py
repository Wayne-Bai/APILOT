from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment()

# Load the template from a file
loader = FileSystemLoader('templates')
env.loader = loader

# Define the template
template = env.get_template('my_template.html')

# Define the context
context = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Render the template with the context
rendered_template = template.render(context)

# Print the rendered template
print(rendered_template)
