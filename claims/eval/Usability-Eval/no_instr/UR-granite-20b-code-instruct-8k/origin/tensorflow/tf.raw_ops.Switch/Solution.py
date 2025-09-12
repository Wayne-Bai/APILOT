import tensorflow as tf

# Define input and predicate
input_tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
predicate = tf.constant([True, False], dtype=tf.bool)

# Use tf.raw_ops.PartitionedCall to forward data to output port determined by predicate
output_tensor = tf.raw_ops.PartitionedCall(
    args=[input_tensor, predicate],
    partitioned_args=[],
    f=lambda x: tf.where(x, x*2, x/2),
    num_returns=1,
    Tout=[tf.float32]
)

# Print the output tensor
print(output_tensor)
