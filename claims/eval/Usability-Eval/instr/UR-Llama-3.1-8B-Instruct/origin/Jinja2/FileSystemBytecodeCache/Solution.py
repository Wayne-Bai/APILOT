from jinja2 import Template
from jinja2.errors import TemplateError
import bytes
import os

# Jinja2 template to render the cache filename
template = Template('''
{{ cache_dir }}/{{ filename }}
''')

def create_bytecode_cache(cache_dir, filename_pattern, data):
    """
    Creates a bytecode cache file in the specified directory.

    Args:
    - cache_dir (str): The directory where the cache items are stored.
    - filename_pattern (str): A pattern string used to build the filename.
    - data (bytes): The bytecode data to be cached.

    Returns:
    - str: The path to the created cache file.
    """
    # Render the filename using the Jinja2 template
    try:
        filename = template.render(cache_dir=cache_dir, filename=filename_pattern)
    except TemplateError as e:
        raise ValueError("Error rendering filename template: {}".format(e))

    # Ensure the cache directory exists
    os.makedirs(cache_dir, exist_ok=True)

    # Create the cache file
    cache_path = os.path.join(cache_dir, filename)
    with open(cache_path, 'wb') as f:
        f.write(data)

    return cache_path

# Example usage:
cache_dir = './bytecode_cache'
filename_pattern = 'bytecode_{{ execution_id }}.bin'
execution_id = 123

bytecode_data = b'\x00\x01\x02\x03'  # example bytecode data
cache_path = create_bytecode_cache(cache_dir, filename_pattern, bytecode_data)
print(cache_path)  # Output:./bytecode_cache/bytecode_123.bin
