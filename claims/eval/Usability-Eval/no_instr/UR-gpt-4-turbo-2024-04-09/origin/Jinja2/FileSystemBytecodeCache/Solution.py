import os
import hashlib
from jinja2 import Environment, FileSystemLoader
from jinja2.bccache import FileSystemBytecodeCache

class CustomFileSystemBytecodeCache(FileSystemBytecodeCache):
    def __init__(self, directory, pattern):
        super().__init__(directory, pattern)

    def _get_cache_filename(self, bucket):
        # Generate a filename based on a pattern
        filename = self.pattern.format(
            hash=hashlib.sha1(bucket.key.encode('utf-8')).hexdigest())
        return os.path.join(self.directory, filename)

# Usage example:
directory = '/path/to/cache/dir'
pattern = 'cache_{hash}.jinja'

# Initialize the cache system
bytecode_cache = CustomFileSystemBytecodeCache(directory, pattern)

# Setup Jinja2 environment with the cache
env = Environment(
    loader=FileSystemLoader('/path/to/templates'),
    bytecode_cache=bytecode_cache
)

# Load a template
template = env.get_template('example_template.html')

# Render the template
rendered = template.render(some_var='value')
