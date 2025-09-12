from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment()

# Load the template
loader = FileSystemLoader('templates')
env.loader = loader

# Define the template
template = env.get_template('overlay_env.j2')

# Define the data to be shared
data = {
    'cache': {},
    'overridden_attributes': {'attr1': 'value1', 'attr2': 'value2'}
}

# Render the template with the data
output = template.render(data=data)

# Print the output
print(output)
