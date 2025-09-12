import tensorflow as tf

class MeshConfiguration:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def represent(self):
        return tf.meshgrid(*self.dimensions)

# Example usage
mesh_config = MeshConfiguration([tf.linspace(-10, 10, 100), tf.linspace(-10, 10, 100)])
mesh = mesh_config.represent()
print(mesh)  # Print the mesh configuration
