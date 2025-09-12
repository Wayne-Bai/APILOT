
from jinja2 import Environment, Template

# Create a new Jinja2 environment
env = Environment()

# Define the attributes that should be shared with the overlay
shared_attrs = ['extensions', 'cache']

# Override the cache attribute with a custom value
env.cache = {'my-extension': 'custom-value'}

# Create a new overlay environment that shares all data except for the overridden attributes
overlay_env = env.clone()

# Add extra extensions to the overlay environment
extra_extensions = ['my-extension', 'another-extension']
for extension in extra_extensions:
    overlay_env.add_extension(extension)
