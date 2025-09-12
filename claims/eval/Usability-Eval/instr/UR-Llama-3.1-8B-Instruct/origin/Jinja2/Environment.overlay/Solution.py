from jinja2 import Environment, DictLoader

# Create a new environment
env = Environment(loader=DictLoader({}))

# Define a function to create a new overlay environment
def create_overlay_env(base_env, extra_extensions=None):
    """
    Create a new overlay environment that shares all the data with the current environment
    except for cache and the overridden attributes. Extensions cannot be removed for an 
    overlayed environment. An overlayed environment automatically gets all the extensions 
    of the environment it is linked to plus optional extra extensions.

    :param base_env: The base environment to overlay
    :param extra_extensions: Optional list of extra extensions to add to the overlay environment
    :return: The new overlay environment
    """
    # Create a new dictionary to store the overlay environment's attributes
    overlay_env_opts = {}

    # Copy all attributes from the base environment to the overlay environment
    # except for cache and overridden attributes
    for key, value in base_env._modules.items():
        if key!= 'cache' and not hasattr(value, '__jinja_overridden__'):
            overlay_env_opts[key] = value

    # Add the extra extensions to the overlay environment's options
    if extra_extensions is not None:
        overlay_env_opts['extensions'] = base_env.options.get('extensions', []) + extra_extensions

    # Create a new overlay environment using the loader of the base environment
    overlay_env = Environment(loader=base_env.loader)

    # Set the options for the overlay environment
    overlay_env.options.update(overlay_env_opts)

    return overlay_env

# Usage example:
base_env = Environment(loader=DictLoader({}))
extra_extensions = ['jinja2.ext.do', 'jinja2.ext.loopcontrols']

overlay_env = create_overlay_env(base_env, extra_extensions)
print(overlay_env.options)
