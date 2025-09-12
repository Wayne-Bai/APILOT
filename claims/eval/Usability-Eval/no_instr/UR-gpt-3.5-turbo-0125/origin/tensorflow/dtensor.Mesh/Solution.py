
import tensorflow as tf

class MeshConfiguration:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.mesh = tf.ones(dimensions)

    def print_mesh(self):
        print(self.mesh)

# Define the list of mesh dimensions
mesh_dimensions = [10, 20, 30]

# Create a Mesh Configuration object with the specified dimensions
mesh_config = MeshConfiguration(mesh_dimensions)

# Print the mesh configuration
mesh_config.print_mesh()
