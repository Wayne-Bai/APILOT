from jinja2 import Environment, FileSystemLoader
from jinja2.bytecode import FileSystemBytecodeCache

class MyBytecodeCache(FileSystemBytecodeCache):
    def __init__(self, directory, pattern):
        super().__init__(directory, pattern)

# Example usage:
# Create a bytecode cache that stores bytecode in the 'cache_folder' directory.
# The pattern '{prefix}.{name}.{hash}.bytecode' is used for the filenames.
cache = MyBytecodeCache('cache_folder', '{prefix}.{name}.{hash}.bytecode')

# Configure Jinja2 environment to use the created cache
env = Environment(loader=FileSystemLoader('templates_folder'), bytecode_cache=cache)
