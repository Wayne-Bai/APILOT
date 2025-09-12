import tensorflow as tf

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions
        self.mesh_shape = tf.constant(mesh_dimensions, dtype=tf.int32)

    def get_mesh_shape(self):
        return self.mesh_shape

    def get_mesh_dimensions(self):
        return self.mesh_dimensions

# Example usage
mesh_dimensions = [4, 4]  # Example mesh dimensions
mesh_config = MeshConfig(mesh_dimensions)
print("Mesh Shape:", mesh_config.get_mesh_shape().numpy())
print("Mesh Dimensions:", mesh_config.get_mesh_dimensions())
