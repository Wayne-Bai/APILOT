import tensorflow as tf

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions
        self.mesh_shape = tf.constant(mesh_dimensions, dtype=tf.int32)

    def get_mesh_shape(self):
        return self.mesh_shape

    def get_mesh_dimensions(self):
        return self.mesh_dimensions

# Example usage:
# mesh_dimensions = [4, 4]  # 4x4 mesh
# mesh_config = MeshConfig(mesh_dimensions)
# print(mesh_config.get_mesh_shape())  # TensorShape([4, 4])
# print(mesh_config.get_mesh_dimensions())  # [4, 4]
