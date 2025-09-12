from jinja2 import Environment, FileSystemLoader

class OverlayEnvironment(Environment):
    def __init__(self, environment, **kwargs):
        # Copy existing environment attributes
        loader = kwargs.get('loader', environment.loader)
        extensions = list(environment.extensions.keys())

        # Add any additional extensions specified
        extra_extensions = kwargs.get('extra_extensions', [])
        extensions.extend(extra_extensions)

        # Initialize with copied and overridden attributes
        super().__init__(
            loader=loader,
            extensions=extensions,
            autoescape=kwargs.get('autoescape', environment.autoescape),
            cache_size=kwargs.get('cache_size', environment.cache_size),
            optimized=kwargs.get('optimized', environment.optimized),
            trim_blocks=kwargs.get('trim_blocks', environment.trim_blocks),
            lstrip_blocks=kwargs.get('lstrip_blocks', environment.lstrip_blocks),
            keep_trailing_newline=kwargs.get('keep_trailing_newline', environment.keep_trailing_newline)
        )

        # Override cache specifically for the overlay environment
        self.cache = {}

        # Attributes that are linked and not just copied
        self.filters = environment.filters.copy()
        self.tests = environment.tests.copy()
        self.globals = environment.globals.copy()

# Use case example
# Assume `env` is your original environment
env = Environment(loader=FileSystemLoader('templates'))

# Create an overlay environment with additional extensions
overlay_env = OverlayEnvironment(env, extra_extensions=['jinja2.ext.do'])

# You can now use `overlay_env` similar to `env`
template = overlay_env.get_template('example_template.html')
output = template.render(variable1='value1', variable2='value2')

print(output)
