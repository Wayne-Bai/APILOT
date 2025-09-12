
import tensorflow as tf

# Define the variable
variable = tf.Variable([1, 2, 3, 4, 5], dtype=tf.int32)

# Define the indices
indices = tf.constant([1, 3], dtype=tf.int32)

# Create the Gather operation
gather = tf.raw_ops.Gather(
    resource=variable,
    indices=indices,
    dtype=tf.int32
)

# Print the result
print(gather)
