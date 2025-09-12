from jinja2 import Environment, FileSystemLoader
from jinja2.bccache import FileSystemBytecodeCache

class CustomFileSystemBytecodeCache:
    def __init__(self, cache_dir, pattern='%s.cache'):
        self.cache = FileSystemBytecodeCache(directory=cache_dir, pattern=pattern)

    def get_environment(self, template_folder):
        env = Environment(
            loader=FileSystemLoader(template_folder),
            bytecode_cache=self.cache
        )
        return env

# Usage example
cache_directory = '/path/to/your/cache/directory'
cache_pattern = '%s.jinja2.cache'
template_directory = '/path/to/your/templates'

my_cache = CustomFileSystemBytecodeCache(cache_directory, cache_pattern)
environment = my_cache.get_environment(template_directory)
