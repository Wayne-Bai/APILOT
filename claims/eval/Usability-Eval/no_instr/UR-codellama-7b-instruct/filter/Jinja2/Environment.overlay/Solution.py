
from jinja2 import Environment, OverlayEnvironment

# Create a new overlay environment that shares all the data with the current environment except for cache and the overridden attributes.
overlay_env = OverlayEnvironment(env)

# Extensions cannot be removed for an overlayed environment. An overlayed environment automatically gets all the extensions of the environment it is linked to plus optional extra extensions.
overlay_env.add_extension("some_extension")
