from jinja2 import Environment, select_autoescape
# Create a new overlay environment that shares all the data with the current environment
# except for cache and the overridden attributes
overlay_env = Environment(loader=env.loader,
                         autoescape=select_autoescape(env.autoescape),
                         extensions=env.extensions)
# An overlayed environment automatically gets all the extensions of the environment it is linked to
# plus optional extra extensions
overlay_env.extensions.update(extra_extensions)
