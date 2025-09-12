from jinja2 import Environment, Template, FileSystemLoader, select_autoescape
from jinja2.bccache import FileSystemBytecodeCache

# Initialize a Jinja2 Environment with FileSystemBytecodeCache
def create_jinja_env(cache_dir, pattern):
    bytecode_cache = FileSystemBytecodeCache(cache_dir, pattern)
   
    # Create a Jinja2 environment
    env = Environment(
        loader=FileSystemLoader('/path/to/templates'),  # Set the path to your template directory
        autoescape=select_autoescape(['html', 'xml']),
        bytecode_cache=bytecode_cache
    )
    
    return env

# Example usage
cache_directory = '/path/to/cache'
filename_pattern = '__jinja2_cache_%s.cache'
env = create_jinja_env(cache_directory, filename_pattern)

# Assuming you have a template named 'example.html'
template = env.get_template('example.html')

# Render the template with context variables
rendered = template.render(variable1='value1', variable2='value2')

print(rendered)
