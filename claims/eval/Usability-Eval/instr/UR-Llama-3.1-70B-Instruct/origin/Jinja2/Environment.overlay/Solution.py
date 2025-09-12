from jinja2 import Environment, OverlayEnvironment

# Create the original environment
env = Environment()

# Create an overlay environment that shares all data except for cache and overridden attributes
overlay = OverlayEnvironment(env, block_start_string='{%', trim_blocks=True, cache_size=0)

# The original environment and the overlay environment share all filters, tests, and functions
env.filters['custom_filter'] = lambda x: x.upper()

# The filter is available in both environments
print(env.filters['custom_filter'])  # prints: <function __main__.<lambda>>
print(overlay.filters['custom_filter'])  # prints: <function __main__.<lambda>>

# But if we modify a attribute that is just copied over on creation of the overlay
# the change does not follow through to the overlay
env.block_start_string = '<%'

print(env.block_start_string)  # prints: <% 
print(overlay.block_start_string)  # prints: {% 
# still the old value of the original environment at creation of the overlay

# But some attributes like extensions are truly linked and can be added in the overlay
class MyExtension:
    def __init__(self, environment):
        environment.globals['my_extension_global'] ='my_extension_global'
        environment.filters['my_extension_filter'] = lambda x: x.upper() + '!'

# Add the extension to the overlay
overlay.add_extension(MyExtension)

# The extension is available in both environments
print(env.globals['my_extension_global'])  # prints: my_extension_global
print(overlay.globals['my_extension_global'])  # prints: my_extension_global
