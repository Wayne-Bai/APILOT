from jinja2 import Environment, FileSystemLoader
from jinja2.bccache import FileSystemBytecodeCache

class CustomBytecodeCache(FileSystemBytecodeCache):
    def __init__(self, directory, pattern):
        super().__init__(directory, pattern=pattern)

# Example usage:
# Create an environment with a bytecode cache
env = Environment(
    loader=FileSystemLoader('templates'),
    bytecode_cache=CustomBytecodeCache('cache_directory', '__jinja2_bc_%s.cache')
)

# Load a template from the environment
template = env.get_template('example_template.html')

# Render the template with variables
rendered_output = template.render(var1='value1', var2='value2')

# Print the rendered output
print(rendered_output)
