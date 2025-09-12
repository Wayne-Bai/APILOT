from jinja2 import Environment, FileSystemLoader

# Create an Environment object which allows us to load templates
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('my_template.txt')

# Render the template with a context
output = template.render(name='World')

print(output)
