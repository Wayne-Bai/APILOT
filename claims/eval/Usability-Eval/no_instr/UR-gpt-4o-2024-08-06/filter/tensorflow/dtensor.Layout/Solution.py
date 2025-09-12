import tensorflow as tf

# Define a DTensor layout
# For this example, assume we're working with a 2D tensor and a simple mesh across 4 devices

# Create a mesh configuration
mesh = tf.experimental.dtensor.create_mesh(
    devices=["CPU:0", "CPU:1", "CPU:2", "CPU:3"], 
    mesh_dimensions=[("x", 2), ("y", 2)]
)

# Create a simple layout for a 2D tensor
layout = tf.experimental.dtensor.Layout(
    ["x", "y"],  # Each dimension is distributed across the mesh
    mesh
)

# Print layout details
print("Layout information:")
print(f"Sharding Spec: {layout.sharding_spec}")
print(f"Mesh: {layout.mesh}")

# Example usage with a tf.experimental.dtensor.DTensor
tensor = tf.experimental.dtensor.pack(
    components=[tf.constant([[1, 2], [3, 4]])] * 4,
    layout=layout
)

# Operations on the DTensor
result = tensor + 10
print("Result after adding 10 to each element in DTensor:")
tf.print(result)
