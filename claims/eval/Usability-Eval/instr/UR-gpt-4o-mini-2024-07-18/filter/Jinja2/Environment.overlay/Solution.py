from jinja2 import Environment, FileSystemLoader

class OverlayEnvironment:
    def __init__(self, base_env, extensions=None):
        self.base_env = base_env
        self.extensions = extensions if extensions else []
        self.overlay_env = self.create_overlay()

    def create_overlay(self):
        # Copy data from the base environment except for specific attributes
        overlay_data = {key: value for key, value in self.base_env.__dict__.items()
                        if key not in ['cache', 'overridden_attributes']}

        # Create a new Jinja2 environment with overlay data
        overlay_env = Environment(
            loader=FileSystemLoader(self.base_env.loader.searchpath),
            extensions=self.base_env.extensions + self.extensions
        )
        
        # Update overlay environment's attributes with base environment's attributes
        overlay_env.__dict__.update(overlay_data)
        return overlay_env

# Example of how to use the OverlayEnvironment
if __name__ == '__main__':
    # Setting up the initial environment
    base_env = Environment(loader=FileSystemLoader('templates'), extensions=['some_extension'])
    
    # Create an overlay environment with additional extensions
    my_overlay_env = OverlayEnvironment(base_env, extensions=['additional_extension'])

    # You can now use my_overlay_env to render templates with shared data
