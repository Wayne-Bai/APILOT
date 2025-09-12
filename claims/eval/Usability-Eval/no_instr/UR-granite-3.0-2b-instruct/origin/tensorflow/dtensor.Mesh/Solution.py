import tensorflow as tf

class MeshConfig:
    def __init__(self, mesh_dimensions):
        self.mesh_dimensions = mesh_dimensions

    def create_mesh(self):
        mesh_shape = [dim * 2 for dim in self.mesh_dimensions]
        mesh = tf.constant(mesh_shape, dtype=tf.int32)
        return mesh

# Example usage:
mesh_dimensions = [2, 3, 4]
mesh_config = MeshConfig(mesh_dimensions)
mesh = mesh_config.create_mesh()
print(mesh)
