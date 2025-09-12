from jinja2 import Environment, FileSystemLoader

# Create an initial environment
env = Environment(loader=FileSystemLoader('templates'))

# Specify the attributes for the overlay environment
overlay_attributes = {
    'some_attribute': 'some_value',
    'another_attribute': 'another_value'
}

# Create the overlay environment
overlay_env = Environment(
    loader=env.loader,
    base_env=env,
    **overlay_attributes
)

# Define a template to demonstrate the overlay
def overlay_template(text):
    return text

# Apply the overlay template
result = overlay_template('Overlayed value')
print(result)
