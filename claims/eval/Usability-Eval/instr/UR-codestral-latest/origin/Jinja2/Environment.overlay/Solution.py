from jinja2 import Environment, FileSystemLoader

class BaseEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(BaseEnvironment, self).__init__(*args, **kwargs)
        self.shared_data = {}

    def create_overlay(self, overridden_attributes):
        overlay = self.overlay()
        overlay.shared_data = self.shared_data.copy()
        overlay.shared_data.update(overridden_attributes)
        return overlay

# Set up the initial environment
env = BaseEnvironment(loader=FileSystemLoader('/path/to/templates'))
env.shared_data = {'data': 'shared data'}

# Create an overlay environment
overlay_env = env.create_overlay({'data': 'overridden data'})

# Check the shared data in the overlays
print(env.shared_data)  # Output: {'data': 'shared data'}
print(overlay_env.shared_data)  # Output: {'data': 'overridden data'}
