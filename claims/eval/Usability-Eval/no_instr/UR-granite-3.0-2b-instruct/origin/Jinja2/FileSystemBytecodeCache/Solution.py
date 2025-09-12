import os
from jinja2 import Template

# Load the template
template = Template("""
{{ directory }}/{{ pattern }}.pyb
""")

def generate_bytecode_cache_filename(directory, pattern):
    # Generate the filename using the template
    filename = template.render(directory=directory, pattern=pattern)

    # Calculate the full path to the file
    full_path = os.path.join(directory, filename)

    return full_path

# Example usage
directory = "/path/to/cache"
pattern = "my_module"

cache_filename = generate_bytecode_cache_filename(directory, pattern)
print(cache_filename)
