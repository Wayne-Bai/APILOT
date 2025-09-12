from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.bccache import FileSystemBytecodeCache

class CustomFileSystemBytecodeCache(FileSystemBytecodeCache):
    def __init__(self, cache_dir, pattern):
        # Initialize with the directory and filename pattern
        super().__init__(cache_dir=cache_dir, pattern=pattern)

# Example usage
if __name__ == "__main__":
    # Define the directory and pattern for bytecode cache
    cache_directory = './bytecode_cache'
    filename_pattern = '__jinja2_%s.cache'

    # Create a bytecode cache object
    bytecode_cache = CustomFileSystemBytecodeCache(cache_dir=cache_directory, pattern=filename_pattern)

    # Create an environment with the bytecode cache
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']),
        bytecode_cache=bytecode_cache
    )

    # Example rendering
    template = env.get_template('example_template.html')
    output = template.render(your_variable='Hello, Jinja2!')
    print(output)
