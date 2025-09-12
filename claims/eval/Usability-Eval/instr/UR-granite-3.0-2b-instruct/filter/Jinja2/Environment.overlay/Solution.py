from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the base environment (e.g., a dictionary)
base_env = {
    'cache': 'value1',
    'overridden_attr': 'value2',
    'extension1': 'value3',
    'extension2': 'value4'
}

# Define the overlay environment
overlay_env = {}

# Create a Jinja2 template for the overlay environment
template = env.from_string("""
{% for key, value in base_env.items() %}
    overlay_env[{{ key }}] = {{ value }}
{% endfor %}
""")

# Render the template with the base environment
rendered_template = template.render(base_env=base_env)

# Evaluate the rendered template as a Python dictionary
overlay_env = eval(rendered_template)

# Print the overlay environment
print(overlay_env)
