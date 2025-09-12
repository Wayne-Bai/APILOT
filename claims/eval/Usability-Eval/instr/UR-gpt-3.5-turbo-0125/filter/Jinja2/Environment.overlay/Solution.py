
from jinja2 import Environment, PackageLoader

# Create the initial environment
base_env = Environment(loader=PackageLoader('your_package', 'templates'))

# Create the overlay environment
overlay_env = base_env.overlay()

# Share all data except cache and overridden attributes
for key, value in base_env.__dict__.items():
    if key not in ['cache', 'globals', 'templates']:
        setattr(overlay_env, key, value)
