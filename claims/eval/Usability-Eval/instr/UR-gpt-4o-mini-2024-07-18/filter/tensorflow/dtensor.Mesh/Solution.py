import tensorflow as tf

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions
        self.mesh = self.create_mesh()

    def create_mesh(self):
        # Create a mesh based on the provided dimensions
        return tf.constant(self.mesh_dimensions, dtype=tf.float32)

    def get_mesh(self):
        return self.mesh

# Example usage
mesh_dimensions = [2, 3, 4]  # Replace with desired dimensions
mesh_config = MeshConfig(mesh_dimensions)
print(mesh_config.get_mesh())
