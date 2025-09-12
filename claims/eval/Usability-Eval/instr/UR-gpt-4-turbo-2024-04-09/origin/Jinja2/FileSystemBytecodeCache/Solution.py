from jinja2 import Environment, FileSystemLoader
from jinja2.bccache import FileSystemBytecodeCache

# Define the directory and pattern for the cache
cache_directory = 'path/to/cache/directory'
pattern = 'cache_%s.jinja'

# Create a FileSystemBytecodeCache object with the specified directory and pattern
bytecode_cache = FileSystemBytecodeCache(cache_directory, pattern)

# Setup Jinja2 environment with the cache
env = Environment(
    loader=FileSystemLoader('/path/to/templates'),
    bytecode_cache=bytecode_cache
)

# Now you can load and render templates, and they will utilize the bytecode cache.
template = env.get_template('mytemplate.html')
print(template.render(some_var='This is a test'))
