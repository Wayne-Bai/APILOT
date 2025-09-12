
from jinja2 import Environment, PackageLoader

# Define the current environment
current_env = Environment(loader=PackageLoader('myapp', 'templates'))

# Create a new overlay environment based on the current environment
def create_overlay_environment(base_env, cache=None, **overrides):
    overlay_env = Environment(
        loader=base_env.loader,
        extensions=base_env.extensions.copy(),
        cache_size=base_env.cache_size if cache is None else cache,
        **overrides
    )
    return overlay_env

# Example of creating a new overlay environment
overlay_env = create_overlay_environment(current_env, cache=0, trim_blocks=True, lstrip_blocks=True)
