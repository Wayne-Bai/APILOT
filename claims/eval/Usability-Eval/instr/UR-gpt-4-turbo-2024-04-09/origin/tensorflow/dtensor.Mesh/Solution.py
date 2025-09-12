import tensorflow as tf

def mesh_configuration(mesh_dimensions):
    mesh = tf.meshgrid(*mesh_dimensions, indexing='ij')
    return mesh

# Example usage:
dimensions = [tf.range(0, 5), tf.range(0, 5), tf.range(0, 5)]
mesh_config = mesh_configuration(dimensions)
print("Mesh configuration:", mesh_config)
