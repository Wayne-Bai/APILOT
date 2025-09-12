from jinja2 import Environment, FileSystemLoader

# Initialize the Environment and Load the FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

# Specify the bytecode cache directory and cache filename pattern
env.bytecode_cache = env.PathCache('bytecache')

# Use the environment to load and render a template
template = env.get_template('mytemplate.html')
output = template.render(name='John Doe')

# Print the output
print(output)
