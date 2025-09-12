from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the template
template = env.get_template('template.j2')

# Define the context
context = {'key': 'value'}

# Render the template with the context
rendered_template = template.render(context)

# Print the rendered template
print(rendered_template)
