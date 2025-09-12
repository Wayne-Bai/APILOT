from jinja2 import Environment, FileSystemLoader

# Define the path to the Jinja2 templates
template_path = 'path_to_your_template_dir'

# Create a new Jinja2 environment
env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True)

# Define the variables for the template
variables = {
    'cache': 'No Cache Override',
    'overridden_attributes': 'No Override',
}

# Load the template
template = env.get_template('overlay_env_template.j2')

# Render the template with the given variables
overlay_env = template.render(**variables)

print(overlay_env)
