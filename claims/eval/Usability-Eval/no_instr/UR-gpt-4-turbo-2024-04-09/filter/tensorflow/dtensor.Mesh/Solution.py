import tensorflow as tf

class MeshConfig:
    def __init__(self, dimensions):
        # Store the dimensions of the mesh
        self.dimensions = dimensions
    
    def get_config_tensor(self):
        # Create a tensor to represent the mesh dimensions
        return tf.constant(self.dimensions, dtype=tf.int32)

# Example usage:
mesh_dimensions = [8, 8]  # Define your mesh dimensions
mesh_config = MeshConfig(mesh_dimensions)
config_tensor = mesh_config.get_config_tensor()
print("Mesh Configuration Tensor:", config_tensor)
