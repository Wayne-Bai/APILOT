from jinja2 import Environment, FileSystemLoader

class OverlayEnvironment:
    def __init__(self, base_env, extra_extensions=None):
        self.base_env = base_env
        self.extra_extensions = extra_extensions or []
        self.overlay_env = self.create_overlay()

    def create_overlay(self):
        # Create a new environment based on the base one
        new_env = Environment(loader=self.base_env.loader)

        # Share all filters and globals from base environment
        new_env.filters.update(self.base_env.filters)
        new_env.globals.update(self.base_env.globals)

        # Copy extensions, ensuring base extensions and additional extensions are included
        for ext in self.base_env.extensions:
            new_env.add_extension(ext)
        
        # Add extra extensions
        for ext in self.extra_extensions:
            new_env.add_extension(ext)

        # Set up necessary attributes from the base environment,
        # while avoiding cache and overridden attributes
        new_env.autoescape = self.base_env.autoescape
        new_env.extensions = self.base_env.extensions.copy()  # Copy to avoid modifying the original
        
        # Note: Cache-related attributes avoided as per requirements

        return new_env

# Example usage:
if __name__ == "__main__":
    # Setting up the base environment
    base_env = Environment(loader=FileSystemLoader('templates'))
    
    # Creating an overlay environment
    overlay_env = OverlayEnvironment(base_env, extra_extensions=['jinja2.ext.loopcontrols']).overlay_env
    
    # Now overlay_env can be used with shared data and characteristics from base_env
