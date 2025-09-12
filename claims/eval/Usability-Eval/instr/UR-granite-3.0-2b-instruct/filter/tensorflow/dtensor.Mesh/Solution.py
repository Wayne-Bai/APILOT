import tensorflow as tf

class MeshConfig:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def create_mesh(self, num_nodes):
        mesh_size = [d // num_nodes for d in self.dimensions]
        mesh = tf.SparseTensor(indices=tf.random.uniform(shape=(num_nodes, num_nodes), minval=0, maxval=num_nodes-1, dtype=tf.int32),
                             values=tf.random.uniform(shape=(num_nodes, num_nodes), minval=0, maxval=num_nodes-1, dtype=tf.int32),
                             dense_shape=(num_nodes, num_nodes))
        return mesh

# Example usage:
dimensions = [4, 4, 4]
mesh_config = MeshConfig(dimensions)
mesh = mesh_config.create_mesh(8)
