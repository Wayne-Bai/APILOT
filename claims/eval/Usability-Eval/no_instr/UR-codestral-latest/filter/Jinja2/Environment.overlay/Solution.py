import copy

class Environment:
    def __init__(self, data, cache, attributes):
        self.data = data
        self.cache = cache
        self.attributes = attributes
        self.extensions = []

    def add_extension(self, extension):
        self.extensions.append(extension)

def create_overlay(original_env, overridden_attributes):
    overlay_env = copy.copy(original_env)
    overlay_env.cache = {}  # create a new empty cache
    overlay_env.attributes = {**original_env.attributes, **overridden_attributes}
    return overlay_env

# Usage
original_env = Environment(data={}, cache={}, attributes={})
original_env.add_extension('extension1')

overlay_env = create_overlay(original_env, {'attr1': 'value1'})
