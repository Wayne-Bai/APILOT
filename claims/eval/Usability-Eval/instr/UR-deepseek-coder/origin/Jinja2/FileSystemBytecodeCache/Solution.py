from jinja2 import Environment, FileSystemLoader, BytecodeCache
import os

class FileSystemBytecodeCache(BytecodeCache):
    def __init__(self, directory, pattern):
        self.directory = directory
        self.pattern = pattern

    def load_bytecode(self, bucket):
        filename = os.path.join(self.directory, self.pattern % bucket.key)
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                bucket.load_bytecode(f)

    def dump_bytecode(self, bucket):
        filename = os.path.join(self.directory, self.pattern % bucket.key)
        with open(filename, 'wb') as f:
            bucket.write_bytecode(f)

# Example usage
cache_dir = '/path/to/cache/directory'
cache_pattern = 'cachefile_%s.cache'

bytecode_cache = FileSystemBytecodeCache(cache_dir, cache_pattern)
env = Environment(loader=FileSystemLoader('/path/to/templates'), bytecode_cache=bytecode_cache)

# Now you can use the environment to render templates with bytecode caching
template = env.get_template('example.html')
rendered_template = template.render(some_data='Hello, World!')
print(rendered_template)
