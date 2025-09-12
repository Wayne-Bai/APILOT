from jinja2 import Environment, FileSystemBytecodeCache

# Define the directory and pattern
cache_directory = 'bytecode_cache'
filename_pattern = '%s.cache'

# Create a bytecode cache that uses the filesystem
bytecode_cache = FileSystemBytecodeCache(cache_directory, filename_pattern)

# Create an environment and use the bytecode cache
env = Environment(bytecode_cache=bytecode_cache)

# Example usage with the environment
template = env.from_string('Hello {{ name }}!')
rendered = template.render(name='World')

print(rendered)
