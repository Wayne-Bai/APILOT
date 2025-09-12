from jinja2 import Environment, BaseLoader

class OverlayEnvironment(Environment):
    def __init__(self, original_env, cache=None, attribute_overrides=None, extra_extensions=None):
        # If no cache is provided, set to None
        if cache is None:
            cache = {}
        
        # If no attribute overrides are provided, set to an empty dictionary
        if attribute_overrides is None:
            attribute_overrides = {}
        
        # If no extra extensions are specified, set to an empty list
        if extra_extensions is None:
            extra_extensions = []

        # The construction of the overlay environment takes shared data from the original environment
        # The overridden attributes are updated with any provided attribute overrides
        # The extensions are combined from the original environment plus any extra extensions
        super(OverlayEnvironment, self).__init__(
            loader=original_env.loader,
            autoescape=original_env.autoescape,
            cache_size=0,  # Overriding the cache
            extensions=original_env.extensions + extra_extensions,
            **{**{k: getattr(original_env, k) for k in vars(original_env) if k not in attribute_overrides}, **attribute_overrides}
        )

# Example usage
# original_environment = Environment(loader=BaseLoader(), autoescape=True)
# overlay_env = OverlayEnvironment(original_env=original_environment, attribute_overrides={'auto_reload': True})
