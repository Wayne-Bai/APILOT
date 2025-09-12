import tensorflow as tf

# Define a list of Mesh Dimensions, for example, 2D mesh
mesh_dimensions = [('x', 4), ('y', 2)]

# Create a Mesh configuration using tf.experimental.dtensor.Mesh
# Please note, you need to have a DTensor context if using TF DTensor APIs
mesh = tf.experimental.dtensor.Mesh(
    mesh_dims=mesh_dimensions,
    devices=tf.experimental.dtensor.local_devices()
)

# Output the mesh configuration
print(f"Mesh Dimensions: {mesh.dim_names}")
print(f"Number of Devices: {len(mesh.devices)}")
