import tensorflow as tf

# Define the Mesh Dimensions
mesh_dims = [10, 20, 30]

# Create a mesh configuration
mesh_config = tf.keras.utils.MeshConfiguration(
    mesh_dims=mesh_dims,
    mesh_density=None,
    mesh_color=None
)
