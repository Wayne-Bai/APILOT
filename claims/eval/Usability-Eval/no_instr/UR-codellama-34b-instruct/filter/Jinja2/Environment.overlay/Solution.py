
from jinja2 import Environment

# Create a new overlay environment that shares all data with the current environment except for cache and overridden attributes
overlay_env = Environment(linked=True)

# Remove extensions from the overlay environment, if any were added by mistake
for extension in overlay_env.extensions:
    del overlay_env.extensions[extension]

# Add optional extra extensions to the overlay environment
# ...
