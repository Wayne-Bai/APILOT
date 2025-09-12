
import tensorflow as tf

# Define a resource variable
resource = tf.Variable([[1, 2], [3, 4]], dtype=tf.int32)

# Define the indices for gathering slices from the resource variable
indices = [[0, 1], [1, 0]]

# Gather slices from the resource variable according to the indices
sliced_resource = tf.raw_ops.Gather(
    resource=resource,
    indices=indices,
    axis=0
)

print(sliced_resource)
