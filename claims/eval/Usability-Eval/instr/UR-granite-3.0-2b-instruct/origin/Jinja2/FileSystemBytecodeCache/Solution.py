from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the template
template = env.get_template('bytecode_cache.j2')

# Define the context
context = {
    'cache_dir': '/path/to/cache',
    'pattern': ' *.py'
}

# Render the template with the context
output = template.render(context)

# Print the rendered template
print(output)
